import sys
def A(): return 'def B(inp): return ["import sys", "def A(): return " + inp.__repr__(), inp]\ndef T(M, w): M.append(w); return M\nfor i in T(B(A()), sys.argv[1]): print(i)'
def B(inp): return ["import sys", "def A(): return " + inp.__repr__(), inp]
def T(M, w): M.append(w); return M
for i in T(B(A()), sys.argv[1]): print(i)
