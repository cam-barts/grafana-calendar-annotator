import rich_click as click
from decouple import config

from . import lib

GRAFANA_BASE_URL = config("GRAFANA_URL", "")
GRAFANA_API_TOKEN = config("GRAFANA_TOKEN", "")
FLATTEN = config("FLATTEN", "")
FLATTEN_DIRECTION = config("FLATTEN_DIRECTION", "start")


# url = "https://cfainstitute.atlassian.net/wiki/rest/calendar-services/1.0/calendar/export/subcalendar/private/556fe20f07413b4a78bcd90770120351d87f5d49.ics" # Release Management Calendar
url = "https://cfainstitute.atlassian.net/wiki/rest/calendar-services/1.0/calendar/export/subcalendar/private/e50c5944a2d01c970265a0c225850c616d820302.ics"  # IT Events Calendar


@click.command()
@click.option(
    "--grafana-url",
    "-g",
    default=GRAFANA_BASE_URL,
    prompt=True,
    show_default=GRAFANA_BASE_URL,
    required=True,
    type=str,
    help="Url of the Grafana instance to populate annotations into",
)
@click.option(
    "--grafana-api-key",
    "-k",
    default=GRAFANA_API_TOKEN,
    prompt=True,
    hide_input=True,
    show_default=GRAFANA_API_TOKEN,
    required=True,
    type=str,
    help="API key to authenticate to the Grafana instance",
)
@click.option(
    "--calendar-url",
    "-c",
    prompt=True,
    required=True,
    type=str,
    help="URL of the ICS Calendar to use to populate events from",
)
@click.option(
    "--flatten/--no-flatten",
    "-f/-nf",
    default=False,
    show_default=True,
    prompt=True,
    required=True,
    type=bool,
    help="Flattening events will create a single time annotation instead of a span",
)
@click.option(
    "--flatten-direction",
    "-fd",
    default="start",
    show_default="start",
    prompt=True,
    required=True,
    type=click.Choice(["start", "end"], case_sensitive=False),
    help="Create the annotation at the start or the end of the event if the event is flattened",
)
@click.option(
    "--tags",
    "-t",
    default=["generated"],
    show_default="generated,",
    multiple=True,
    required=True,
    type=str,
    help="List of tags to add to created annotations",
)
@click.option(
    "--regenerate/--no-regenerate",
    "-r/-nr",
    default=True,
    show_default=True,
    prompt=True,
    required=True,
    type=bool,
    help="Regenerating will delete all annotations that have the same set of tags before creating new annotations",
)
@click.option(
    "--delete-only",
    "-d",
    default=False,
    show_default=True,
    type=bool,
    flag_value=True,
    help="Only delete annotations with tags, do not create new annotations",
)
def cli(
    grafana_url,
    grafana_api_key,
    calendar_url,
    flatten,
    flatten_direction,
    tags,
    regenerate,
    delete_only,
):
    if delete_only or regenerate:
        if click.confirm(
            f"Are you sure you wish to delete the annotations for the following tags?\n{tags}",
            abort=True,
        ):
            lib.delete_annotations_for_tag(grafana_url, grafana_api_key, list(tags))
    if not delete_only:
        events = lib.get_events_timeline_from_url(calendar_url)
        for event in events:
            print(
                lib.generate_annotation_for_event(
                    grafana_url,
                    grafana_api_key,
                    event,
                    list(tags),
                    flatten,
                    flatten_direction,
                )
            )


if __name__ == "__main__":
    cli()
