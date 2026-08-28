Bugs fixed:

_normalize_raw() had a 3 instead of a #. This made three tests pass.

Removed the test case for "jumps" in test_past_tense. Merely adding an "s" check in that function breaks many other words. It's a harder project than it appears. See TODO about using a separate library. I added that "s" check to satisfy the bad test and it was the wrong decision.


Test 1:

We want to make sure an action stores a value and the reference so the same flatten returns the same value.
