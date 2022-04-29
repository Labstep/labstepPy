from labstep.generic.entity.repository import exportEntity


def exportExperimentStep(step, rootPath):
    stepDir = exportEntity(
        step, rootPath)

    # export comment
    notesDir = stepDir.joinpath('notes')
    notes = step.getComments(count=1000)

    for note in notes:
        note.export(
            notesDir)
