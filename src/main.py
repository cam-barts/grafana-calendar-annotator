import ics
import requests
from rich import print


def get_annotations(
    grafana_base_url: str, grafana_api_token: str, tags=[], limit=10000
):
    """Gets Annotations from Grafana

    Args:
        grafana_base_url (str): URL for Grafana instance
        grafana_api_token (str): API Token for Grafana instance
        tag (str, optional): Use this to filter organization annotations. Defaults to None.
        limit (int, optional): Max limit for results returned. Defaults to 10000.

    Returns:
        list: List of Annotations
    """
    url = grafana_base_url + f"/api/annotations?limit={limit}&type=annotation"
    if tags:
        for tag in tags:
            url += f"&tags={tag}"
    headers = {"Authorization": f"Bearer {grafana_api_token}"}
    resp = requests.get(url, headers=headers)
    return resp.json()


def generate_annotation_for_event(
    grafana_base_url: str,
    grafana_api_token: str,
    event: ics.event.Event,
    tags: list[str] = ["generated"],
    flatten: str = "",
    flatten_direction: str = "start",
) -> dict:
    """Generate an Annotation from an ICS event

    Args:
        grafana_base_url (str): URL for Grafana instance
        grafana_api_token (str): API Token for Grafana instance
        event (ics.event.Event): Event to generate an annotation from
        tags (list[str], optional): List of tags to add to the annotation. Defaults to ["generated"].
        flatten (str, optional): Format all day events into single line annotations. Defaults to "".
        flatten_direction (str, optional): For flattened events, create the annotation at the start of the event or the end. Defaults to "start".

    Returns:
        dict: Returned json from API call
    """
    start = event.begin.int_timestamp * 1000  # millisecond resolution
    end = event.end.int_timestamp * 1000  # millisecond resolution

    for category in event.categories:
        tags.append("CAT__" + category.strip().replace(" ", "_"))

    annotation = {"time": "", "text": event.name.strip(), "tags": tags}
    if event.all_day:
        tags.append("all_day")
        if flatten and event.duration.days == 1:
            if flatten_direction.lower() == "end":
                annotation["time"] = end
            else:
                annotation["time"] = start
        else:
            annotation["time"] = start
            annotation["timeEnd"] = end
    else:
        annotation["time"] = start
        annotation["timeEnd"] = end
    url = grafana_base_url + "/api/annotations"
    headers = {"Authorization": f"Bearer {grafana_api_token}"}
    resp = requests.post(url, headers=headers, json=annotation)
    return resp.json()


def delete_annotation(
    grafana_base_url: str, grafana_api_token: str, annotation_id: int
):
    """Delete an Annotation By ID

    Args:
        grafana_base_url (str): URL for Grafana instance
        grafana_api_token (str): API Token for Grafana instance
        annotation_id (int): ID of Annotation to Delete

    Returns:
        dict: Returned json from API call
    """
    url = grafana_base_url + f"/api/annotations/{annotation_id}"
    headers = {"Authorization": f"Bearer {grafana_api_token}"}
    resp = requests.delete(url, headers=headers)
    return resp.json()


def delete_annotations_for_tag(
    grafana_base_url: str, grafana_api_token: str, tags: list[str]
):
    """Deletes all annotations that have a certain tag

    Args:
        grafana_base_url (str): URL for Grafana instance
        grafana_api_token (str): API Token for Grafana instance
        tag (list[str]): Tags for annotations to delete
    """
    annotations = get_annotations(grafana_base_url, grafana_api_token, tags)
    for annotation in annotations:
        print(delete_annotation(grafana_base_url, grafana_api_token, annotation["id"]))


def get_events_timeline_from_url(calendar_url: str):
    """Pull in Events from ICS Calendar

    Args:
        calendar_url (str): URL of the ICS Calendar

    Returns:
        list[ics.event.Event]: List of Calendar Events
    """
    c = ics.Calendar(requests.get(calendar_url).text)
    return list(c.timeline)
