def format_name(full_name: str) -> str:
    surname, name, father_name = full_name.split()

    result = f"{name} {father_name}, {surname}"

    return result

print(format_name("Aliyev Vali G'aniyevich"))