import re
from urllib import request
import tomli
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomli.loads(content)

        project = data["project"]
        dev_dependencies = data.get("dependency-groups", {}).get("dev", [])

        return Project(
            project["name"],
            project["description"],
            project.get("license"),
            [author["name"] for author in project.get("authors", [])],
            [self._package_name(dep)
             for dep in project.get("dependencies", [])],
            [self._package_name(dep) for dep in dev_dependencies]
        )

    def _package_name(self, requirement):
        # "flask>=3.1.3" -> "flask"
        return re.split(r"[<>=!~\[;\s]", requirement)[0]
