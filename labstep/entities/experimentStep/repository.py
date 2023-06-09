from labstep.generic.entity.repository import exportEntity
from labstep.constants import UNSPECIFIED


def exportExperimentStep(step, rootPath):
    stepDir = exportEntity(
        step, rootPath)

    # export comment
    notesDir = stepDir.joinpath('notes')
    notes = step.getComments(count=UNSPECIFIED)

    for note in notes:
        note.export(
            notesDir)
