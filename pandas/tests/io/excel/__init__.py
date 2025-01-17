import pytest

pytestmark = [
    pytest.mark.filterwarnings(
        # Looks like tree.getiterator is deprecated in favor of tree.iter
        "ignore:This method will be removed in future versions:"
        "PendingDeprecationWarning"
    ),
    pytest.mark.filterwarnings(
        "ignore:This method will be removed in future versions:DeprecationWarning"
    ),
    # GH 38571
    pytest.mark.filterwarnings(
        "ignore:.*In xlrd >= 2.0, only the xls format is supported:FutureWarning"
    ),
]
