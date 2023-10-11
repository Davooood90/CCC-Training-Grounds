s = input()

num_l = s.count("L")
num_m = s.count("M")

fnum_l = s[:num_l].count("L")
mnum_l = s[num_l:(num_l + num_m)].count("L")
fnum_m = s[:num_l].count("M")
mnum_m = s[num_l:(num_l + num_m)].count("M")

print((num_l - fnum_l) + (num_m - mnum_m - min(fnum_m, mnum_l)))
