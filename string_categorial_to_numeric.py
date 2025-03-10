from veusz.plugins import (DatasetPlugin, Dataset1D, FieldDataset, FieldText, datasetpluginregistry)
from veusz import qtall as qt

def _(text, disambiguation=None, context='DatasetPlugin'):
    return qt.QCoreApplication.translate(context, text, disambiguation)

class StringCategorialToNumeric(DatasetPlugin):
    menu = (_('Convert'), _('String Categorial to Numeric'),)
    name = 'StringCategorialToNumeric'
    description_short = _('Converts categorial string values to numbers')
    description_full = _('Converts categorial string values to numbers.')

    def __init__(self):
       self.fields = [
            FieldDataset('c_in', _('Input dataset (categorial)'), datatype="text"),
            FieldText('n_out', _('Output dataset name (numeric)'))
        ]

    def getDatasets(self, fields):
         if fields['n_out'] == '':
            raise DatasetPluginException(_('Invalid output dataset name'))
        self.n_out = Dataset1D(fields['n_out'])
        return [self.n_out]

    def updateDatasets(self, fields, helper):
        sequence_input = helper.getTextDataset( fields['c_in'] ).data
        mapping = dict([(x,i) for i,x in enumerate(list(dict.fromkeys(sequence_input)))])
        sequence_output = [mapping[x] for x in sequence_input]
        self.n_out.update(data=sequence_output)

datasetpluginregistry += [StringCategorialToNumeric]