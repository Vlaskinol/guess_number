try:
    import practicum
except ImportError: 
    raise AssertionError('Module Practicum is not found')
EXPECTED_FUNC_NAME = 'say_hello'
def test_say_hello_exists():
    assert hasattr(practicum, EXPECTED_FUNC_NAME), (
        f'Function `{EXPECTED_FUNC_NAME}` is not found in module <Practicum>')
def test_say_hello_run_without_exceptions():
    try:
        practicum.say_hello()
    except Exception as error:
        raise AssertionError(
            f'During the `{EXPECTED_FUNC_NAME}` starting'
            f'the exception appeared : {type(error).__name__}: {error}`'
        )
# Check if there is a file with say_hello in code of practicum.py
# Check if this function starts without errors
