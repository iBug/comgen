import subprocess as sp
from datetime import datetime
from . import util


class Git:
    time_format = "%Y-%m-%dT%H:%M:%S"

    @staticmethod
    def commit(message=None, author=None, ctime=None, atime=None):
        if message is None:
            message = util.random_text()
        elif isinstance(message, int):
            message = util.random_text(message)

        cmd = ["git", "commit", "-m", message]
        environ = {}
        if author:
            cmd.extend(["--author", author])
        if ctime:
            if not isinstance(ctime, float) and not isinstance(ctime, int):
                raise TypeError("ctime must be a number")
            environ["GIT_COMMITTER_DATE"] = datetime.fromtimestamp(ctime).strftime(Git.time_format)
        if atime:
            if not isinstance(atime, float) and not isinstance(atime, int):
                raise TypeError("atime must be a number")
            environ["GIT_AUTHOR_DATE"] = datetime.fromtimestamp(atime).strftime(Git.time_format)

        return sp.Popen(cmd, env=environ).communicate()
