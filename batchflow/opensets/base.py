""" Contains the base class for open datasets """
from .. import Dataset, DatasetIndex
from .. import ImagesBatch


class Openset(Dataset):
    """ The base class for open datasets """
    def __init__(self, index=None, batch_class=None, path=None, preloaded=None, **kwargs):
        self._train_index, self._test_index = None, None
        if index is None:
            preloaded, index, self._train_index, self._test_index = self.download(path=path)
        super().__init__(index, batch_class=batch_class, preloaded=preloaded, **kwargs)

        if self._train_index and self._test_index:
            self.train = type(self).from_dataset(self, self._train_index, batch_class=batch_class, **kwargs)
            self.test = type(self).from_dataset(self, self._test_index, batch_class=batch_class, **kwargs)

    @staticmethod
    def uild_index(index):
        """ Create an index """
        if index is not None:
            return super().build_index(index)
        return None

    def download(self, path):
        """ Download a dataset from the source web-site """
        _ = path
        return None
    
    def _infer_train_test_index(self, train_len, test_len):
        total_len = train_len + test_len
        index = DatasetIndex(list(range(total_len)))
        train_index = DatasetIndex(list(range(train_len)))
        test_index = DatasetIndex(list(range(train_len, total_len)))
        return index, train_index, test_index


class ImagesOpenset(Openset):
    """ The base class for open datasets with images """
    def __init__(self, index=None, batch_class=ImagesBatch, *args, **kwargs):
        super().__init__(index, batch_class, *args, **kwargs)
