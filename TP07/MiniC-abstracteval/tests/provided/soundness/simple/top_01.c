int main()
{
	int x;
	assert (x != 0);
	assert (x != 1);
	assert (x != -1);
	assert (x >= -2);
	assert (x > -2);
	assert (x <= 2);
	assert (x < 2);
	assert (x >= 0);
	assert (x <= 0);
	return 0;
}
// EXPECTED
// assert at line 4: failed to verify
// assert at line 5: failed to verify
// assert at line 6: failed to verify
// assert at line 7: failed to verify
// assert at line 8: failed to verify
// assert at line 9: failed to verify
// assert at line 10: failed to verify
// assert at line 11: failed to verify
// assert at line 12: failed to verify