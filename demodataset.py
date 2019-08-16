from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
class DemoDataset(HubDataset):
    """DemoDataset"""
    def __init__(self):
        self.dataset_dir = "D:\PYTHON_PROJECT\sentimentAnalysis\paddledataset\classifer"   #数据文件所在的路径
        self.labels=[]
        self._load_train_examples()
        self._load_test_examples()
        self._load_dev_examples()

    def _load_train_examples(self):
        self.train_file = os.path.join(self.dataset_dir, "train.tsv")
        self.train_examples = self._read_tsv(self.train_file)

    def _load_dev_examples(self):
        self.dev_file = os.path.join(self.dataset_dir, "valid.tsv")
        self.dev_examples = self._read_tsv(self.dev_file)

    def _load_test_examples(self):
        self.test_file = os.path.join(self.dataset_dir, "test.tsv")
        self.test_examples = self._read_tsv(self.test_file)

    def get_train_examples(self):
        return self.train_examples

    def get_dev_examples(self):
        return self.dev_examples

    def get_test_examples(self):
        return self.test_examples

    def get_labels(self):
        """define it according the real dataset"""
        return self.

    @property
    def num_labels(self):
        """
        Return the number of labels in the dataset.
        """
        return len(self.get_labels())

    def _read_tsv(self, input_file, quotechar=None):
        """Reads a tab separated value file."""
        with codecs.open(input_file, "r", encoding="UTF-8") as f:
            reader=f.readlines()
            # reader = csv.reader(f, delimiter="\t", quotechar=quotechar)
            examples = []
            seq_id = 0
            # header = next(reader)  # skip header
            for line in reader:
                if line!="\r\n":
                    line=line.strip("\r").split("    ")
                    if line[3] not in self.label:
                        self.label.append(line[3])
                    example = InputExample(
                        guid=seq_id, label=line[3], text_a=line[1])
                    seq_id += 1
                    examples.append(example)

            return examples
#读取数据
dataset=DemoDataset()
