def _assert_equal(t1, t2):
    if t1 == t2:
        print 'Pass'
        return True

    print 'Failure: expected "{}", found "{}"'.format(t1, t2)
    return False


def runtests(tests, function, inplace=False):
    passed = True
    for test in tests:
        if inplace:
            function(*test[0])
            cur_pass = _assert_equal(test[1], test[0][0])
            passed = passed and cur_pass
        else:
            cur_pass = _assert_equal(test[1], function(*test[0]))
            passed = passed and cur_pass

    if passed:
        print '\n\nYou Win!\n\n'
    else:
        print '\n\nYou Lose :(\n\n'

    return passed
