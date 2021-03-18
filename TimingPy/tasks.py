#!/usr/bin/env python

"""Methods related to the Tasks utilized by the account."""

import TimingPy.timing

class Tasks(TimingPy.timing.Connection):
    """Task specific module actions"""
    def __init__(self, api_key):
        TimingPy.timing.Connection.__init__(self, api_key)
        self.url = self._url("/time-entries")

    def start_new_task(self, #pylint: disable=too-many-arguments
        title,
        start_date=None,
        project=None,
        notes=None
    ):
        """Start a new task."""
        data = {
            'title': title,
            'start_date': start_date,
            'project': project,
            'notes': notes
            }
        return self._post_data(self.url, data)

    def stop_task(self):
        """Stop the currently running task."""
        url = self.url + "/stop"
        data = {}
        return self._put_data(url, data)

    def get_task_list(self, #pylint: disable=too-many-arguments
        start_date_min=None,
        start_date_max=None,
        projects=None,
        search_query=None,
        is_running=None,
        include_project_data=None,
        include_child_projects=None,
        include_team_members=None):
        """Return a list of tasks."""
        url = self.url
        if projects is None:
            projects = []
        data = {
            'start_date_min': start_date_min,
            'start_date_max': start_date_max,
            'projects': projects,
            'search_query': search_query,
            'is_running': is_running,
            'include_project_data': include_project_data,
            'include_child_projects': include_child_projects,
            'include_team_members': include_team_members,
            }
        return self._get_data(url, data)

    def create_new_task(self, #pylint: disable=too-many-arguments
        title,
        start_date,
        end_date,
        project=None,
        notes=None
    ):
        """Display the specified task."""
        data = {
            'start_date': start_date,
            'end_date': end_date,
            'project': project,
            'title': title,
            'notes': notes
            }
        return self._post_data(self.url, data)

    def get_task(self, task):
        """Display the specified task."""
        url = self.url + "/" + task
        return self._get_data(url)

    def update_task(self, #pylint: disable=too-many-arguments
        task,
        title=None,
        start_date=None,
        end_date=None,
        project=None,
        notes=None
    ):
        """Update the specified task."""
        url = self.url + "/" + task
        data = {
            'start_date': start_date,
            'end_date': end_date,
            'project': project,
            'title': title,
            'notes': notes
            }
        return self._put_data(url, data)

    def delete_project(self, task):
        """Delete the specified task."""
        url = self.url + "/" + task
        return self._delete_data(url)
