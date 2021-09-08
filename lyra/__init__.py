import sys
from pathlib import Path
sys.path.insert(0, str(Path('__file__').resolve().parent))

from lyra._base.classifier import Classifier
from lyra._base.error import AttributeDoesNotExist

from lyra._base.data import water, linearData
from lyra._base.utils import bootfold, coefficient, show_accuracy, evaluate_classif, \
                        writeout, get_table_cols, split
                    