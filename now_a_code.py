def hey_you(**sneha):
    total=sum(sneha.values())
    number_of_subject=len(sneha)
    ratio=total / number_of_subject
    return ratio

for boys,sneha in sneha_dich.items():
    ratio = calculate_ratio(**sneha)
    print(f"{boys}: {ratio:.2f}%")
    