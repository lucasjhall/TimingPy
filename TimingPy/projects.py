#!/usr/bin/env python

"""Methods related to the Projects utilized by the account."""

import TimingPy.timing

class Projects(TimingPy.timing.Connection):
    """Project specific module actions"""
    def __init__(self, api_key):
        TimingPy.timing.Connection.__init__(self, api_key)
        self.url = self._url("/projects")

    def get_projects(self): #pylint: disable=no-self-use
        """Return a list containing all projects.."""
        url = self.url
        return self._get_data(url)

    def get_hierarchy(self):
        """Return the complete project hierarchy."""
        url = self.url + "/hierarchy"
        return self._get_data(url)

    def create_project(self, #pylint: disable=too-many-arguments
        title,
        parent=None,
        color=None,
        productivity_score=None,
        is_archived=None
    ):
        """Create a new project."""
        data = {
            'title': title,
            'parent': parent,
            'color': color,
            'productivity_score': productivity_score,
            'is_archived': is_archived
            }
        return self._post_data(self.url, data)

    def get_project(self, project):
        """Display the specified project."""
        url = self.url + "/" + project
        return self._get_data(url)

    def update_project(self, #pylint: disable=too-many-arguments
        project,
        title=None,
        color=None,
        productivity_score=None,
        is_archived=None
    ):
        """Update the specified project."""
        data = {
            'title': title,
            'color': color,
            'productivity_score': productivity_score,
            'is_archived': is_archived
            }
        url = self.url + "/" + project
        return self._patch_data(url, data)

    def delete_project(self, project):
        """Delete the specified project and all of its children."""
        url = self.url + "/" + project
        return self._delete_data(url)
