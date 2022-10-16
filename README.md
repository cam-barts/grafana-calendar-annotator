# Grafana Calendar Annotator

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6552/badge)](https://bestpractices.coreinfrastructure.org/projects/6552)

Generate [annotations](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/) in Grafana from events pulled from an ICS calendar.

## Hacktoberfest

This project welcomes [Hacktoberfest](https://hacktoberfest.com/) contributions! Any contributions to increase the [OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/en/projects/6552) percentage or that [close an issue](https://github.com/cam-barts/grafana-calendar-annotator/issues) will be given priority.

## Getting Started

### CLI

```bash
$ grafana-calendar-annotator --help

 Usage: grafana-calendar-annotator [OPTIONS]

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --grafana-url                 -g      TEXT         Url of the Grafana instance to populate annotations into    │
│                                                       [required]                                                  │
│ *  --grafana-api-key             -k      TEXT         API key to authenticate to the Grafana instance [required]  │
│ *  --calendar-url                -c      TEXT         URL of the ICS Calendar to use to populate events from      │
│                                                       [required]                                                  │
│ *  --flatten/--no-flatten        -f/-nf               Flattening events will create a single time annotation      │
│                                                       instead of a span                                           │
│                                                       [default: no-flatten]                                       │
│                                                       [required]                                                  │
│ *  --flatten-direction           -fd     [start|end]  Create the annotation at the start or the end of the event  │
│                                                       if the event is flattened                                   │
│                                                       [default: (start)]                                          │
│                                                       [required]                                                  │
│ *  --tags                        -t      TEXT         List of tags to add to created annotations                  │
│                                                       [default: (generated,)]                                     │
│                                                       [required]                                                  │
│ *  --regenerate/--no-regenerate  -r/-nr               Regenerating will delete all annotations that have the same │
│                                                       set of tags before creating new annotations                 │
│                                                       [default: regenerate]                                       │
│                                                       [required]                                                  │
│    --delete-only                 -d                   Only delete annotations with tags, do not create new        │
│                                                       annotations                                                 │
│    --help                                             Show this message and exit.                                 │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

The following flags can be set with environment variables:

| Flag                | Variable Name     |
| ------------------- | ----------------- |
| --grafana-url       | GRAFANA_URL       |
| --grafana-api-key   | GRAFANA_TOKEN     |
| --flatten           | FLATTEN           |
| --flatten-direction | FLATTEN_DIRECTION |

```bash
grafana-calendar-annotator --grafana-url https://my-grafana.com --grafana-api-key abcd1234 --flatten --flatten-direction end --calendar-url https://my-calendar.com/personal.ics

# is the same as this

GRAFANA_URL=https://my-grafana.com GRAFANA_TOKEN=abcd1234 FLATTEN=true FLATTEN_DIRECTION=end grafana-calendar-annotator --calendar-url https://my-calendar.com/personal.ics
```


### Installing

#### Pip

For the library and the cli

```shell
pip install grafana_calendar_annotator
```

#### Pipx

Pipx is useful for [installing and running applications in isolated environments](https://pypa.github.io/pipx/). I've always found it useful to ensure python applications are can be executed from anywhere in your system.

```shell
pipx install grafana_calendar_annotator
```

## Running the tests

<!--TODO-->

## Deployment

<!--TODO-->

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used for the Code of Conduct
  - [Poetry](https://python-poetry.org/) - Used for build and packaging
  - [Contributing.md Generator](https://generator.contributing.md/)
  - [Billie Thompson's README Template](https://github.com/PurpleBooth/a-good-readme-template)

## Contributing

Please read [CONTRIBUTING.md](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/cam-barts/grafana-calendar-annotator/tags).

## Contributors

[Contributors](https://github.com/cam-barts/grafana-calendar-annotator/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/LICENSE.txt).