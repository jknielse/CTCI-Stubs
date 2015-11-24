def _assert_equal(t1, t2, quiet):
    if t1 == t2:
        if not quiet:
            print 'Pass'
        return True
    if not quiet:
        print 'Failure: expected "{}", found "{}"'.format(t1, t2)
    return False


def runtests(tests, function=lambda arg: arg, inplace=False, quiet=False):
    passed = True
    for test in tests:
        if inplace:
            function(*test[0])
            cur_pass = _assert_equal(test[1], test[0][0], quiet)
            passed = passed and cur_pass
        else:
            cur_pass = _assert_equal(test[1], function(*test[0]), quiet)
            passed = passed and cur_pass

    if not quiet:
        if passed:
            print '\n\nYou Win!\n\n'
        else:
            print '\n\nYou Lose :(\n\n'

    return passed
