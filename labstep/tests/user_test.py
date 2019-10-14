from ...user import User

testUser = User({api-key: 'api-testing@labstep.com'})


class TestUser:
    def test_get_experiment():
        exp = testUser.getExperiment(1)
        assert exp.name == 'Name of Experiment'
