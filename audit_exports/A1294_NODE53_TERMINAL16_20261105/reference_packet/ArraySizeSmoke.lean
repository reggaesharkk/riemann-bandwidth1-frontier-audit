import Init
def testArray : Array Nat := (List.range 77).toArray
theorem testArray_size : testArray.size = 77 := by decide
#print testArray_size
#print axioms testArray_size
