from pathlib import Path as _Path


class Path(type(_Path())):
    def load(self):
        if self.suffix in {".ipynb"}:
            import nbformat.v4

            return nbformat.v4.reads(self.read_text())
        return self.read_text()

    def dump(self, data):
        if self.suffix in {".ipynb"}:
            import nbformat.v4

            return nbformat.v4.writes(data)
        return self.write_text(data)

    def write(self, data):
        return self.write_text(self.dump(data))
