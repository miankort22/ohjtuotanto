class Project:
    def __init__(self, name, description, license_name, authors,
                 dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license_name
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _list_to_str(self, items):
        return "\n".join(f"- {item}" for item in items)

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n"
            f"\nAuthors:\n{self._list_to_str(self.authors)}\n"
            f"\nDependencies:\n{self._list_to_str(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n"
            f"{self._list_to_str(self.dev_dependencies)}"
        )
