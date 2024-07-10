def dinesh_percentage(*dinesh, total_marks=100):
    if len(dinesh) != 5:
        raise ValueError("Exactly 5 subject marks must be provided.")
    
    per = (sum(dinesh) / (total_marks * 5)) * 100
    per_for = "{:2f}".format(per)
    return {'marks': dinesh, 'per': per}

subject_marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    subject_marks.append(mark)

result = dinesh_percentage(*subject_marks)
print(result)

