init python:
    class FilePageNextTen(Action, DictEquality):
        """
        :doc: file_action

        Goes to the next file page.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to.

        `wrap`
            If true, we can go to the first page when on the
            last file page if `max` is set.

        `auto`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.

        `quick`
            If true and wrap is set, this can bring the player to
            the page of automatic saves.
        """

        alt = _("Next file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True):

            page = persistent._file_page

            if page == "auto":
                if config.has_quicksave and quick:
                    page = "quick"
                else:
                    page = "1"

            elif page == "quick":
                page = "1"

            else:
                page = int(page) + 10

                if max is not None:
                    if page > max:
                        if wrap:
                            if config.has_autosave and auto:
                                page = "auto"
                            elif config.has_quicksave and quick:
                                page = "quick"
                            else:
                                page = "1"
                        else:
                            page = None

                if page is not None:
                    page = str(page)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None

        def predict(self):
            _predict_file_page(self.page)


    class FilePagePreviousTen(Action, DictEquality):
        """
        :doc: file_action

        Goes to the previous file page, if possible.

        `max`
            If set, this should be an integer that gives the number of
            the maximum file page we can go to. This is required to enable
            wrap.

        `wrap`
            If true, we can go to the last page when on the first file page if max is set.

        `auto`
            If true, this can bring the player to
            the page of automatic saves.

        `quick`
            If true, this can bring the player to
            the page of automatic saves.
        """

        alt = _("Previous file page.")

        def __init__(self, max=None, wrap=False, auto=True, quick=True):

            if wrap and max is not None:
                max = str(max)
            else:
                max = None

            page = persistent._file_page

            if page == "auto":
                page = max

            elif page == "quick":
                if config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            elif int(page) < 10:
                if config.has_quicksave and quick:
                    page = "quick"
                elif config.has_autosave and auto:
                    page = "auto"
                else:
                    page = max

            else:
                page = str(int(page) - 10)

            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent._file_page = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page

        def predict(self):
            _predict_file_page(self.page)
