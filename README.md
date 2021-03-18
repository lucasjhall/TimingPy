# TimingPy

TimingPy is a Python library to wrap the web API for [Timing.app][0].  
Timing.app is a [paid][1] macOS app for time tracking.

## API Documentation

[Web API Documentation][2]  
[Timing Web Login][3]

## TimingPy Usage

### Projects

#### Projects Connection

```python
>>> import TimingPy
>>> p = TimingPy.Projects('YOUR_API_KEY')
```

### Query the API for Open Projects

```python
>>> import json # for a cleaner illustration
>>> projs = p.get_projects()
>>> for proj in projs:
...     print(json.dumps(proj))
{
    "self": "/projects/$ID",
    "membership_id": null,
    "title": "$TITLE",
    "title_chain": ["$TITLE"],
    "color": "#FF7B4DFF",
    "productivity_score": 1,
    "is_archived": false,
    "children": [{
        "self": "/projects/$ID"
    }],
    "parent": null
}
{
    "self": "/projects/$ID2",
    "membership_id": null,
    "title": "$TITLE_2",
    "title_chain": ["$TITLE", "$TITLE_2"],
    "color": "#EC4762FF",
    "productivity_score": 1,
    "is_archived": false,
    "children": [],
    "parent": {
        "self": "/projects/$ID"
    }
}
```

### Tasks

#### Tasks Connection

```python
>>> import TimingPy
>>> t = TimingPy.Tasks('YOUR_API_KEY')
```

### Create a new Task vi the API

```python
>>> task = t.create_new_task(
    title="New Task",
    start_date="2021-03-16T16:00:00+0000",
    end_date="2021-03-16T17:00:00+0000")
>>> print(task.status_code)
201
>>> print(task.text)
{
    "data": {
        "self": "\/time-entries\/$ID",
        "start_date": "2021-03-16T16:00:00.000000+00:00",
        "end_date": "2021-03-16T17:00:00.000000+00:00",
        "duration": 3600,
        "project": null,
        "title": "New Task",
        "notes": null,
        "is_running": false,
        "creator_name": "$YOUR_EMAIL"
    }
}
```

## Requirements

### `requests`

As noted in [requirements.txt](./requirements.txt),
`requests` is used for all outbound API calls

[0]: (https://timingapp.com/)  
[1]: (https://timingapp.com/pricing)  
[2]: (https://web.timingapp.com/docs/)  
[3]: (https://web.timingapp.com/login)
