import labstep.generic.entity.repository as entityRepository
from labstep.service.htmlExport import htmlExportService
from labstep.constants import UNSPECIFIED
from labstep.config.export import includePDF
from labstep.service.htmlToPDF import htmlToPDF


def exportProtocolVersion(protocolVersion, root_path):

    protocolVersion.update()

    expDir = entityRepository.exportEntity(protocolVersion, root_path)

    # export notes
    notesDir = expDir.joinpath('notes')
    notes = protocolVersion.getComments(count=UNSPECIFIED)

    for note in notes:
        note.export(notesDir)

    # save inventory fields
    inventoryFieldsDir = expDir.joinpath('inventory')
    inventoryFields = protocolVersion.getInventoryFields()

    for inventoryField in inventoryFields:
        inventoryField.export(inventoryFieldsDir)

    # save data
    dataDir = expDir.joinpath('data')
    data = protocolVersion.getDataFields()

    for dat in data:
        dat.export(dataDir)

    # get html
    html = htmlExportService.getHTML(
        protocolVersion, withImages=includePDF)

    html_with_paths = htmlExportService.insertFilepaths(expDir, html)

    with open(expDir.joinpath(f'{expDir.name}.html'), 'w') as out:
        out.write(html_with_paths)

    # get pdf
    if includePDF:
        pdf = htmlToPDF(protocolVersion.__user__, html)
        with open(expDir.joinpath(f'{expDir.name}.pdf'), 'wb') as out:
            out.write(pdf)
