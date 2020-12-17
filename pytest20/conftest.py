

from datetime import datetime
from py.xml import html
import pytest


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Description"))
    # cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    # cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.th(report.description))
    # cells.insert(1, html.th(datetime.utcnow(), class_="col-time"))
    # cells.pop()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
