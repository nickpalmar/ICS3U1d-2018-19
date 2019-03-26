# squirrel party success

def cigar_party(cigars, is_weekend):
    if is_weekend == False and (cigars >= 40 and cigars <= 60):
        print("True")
    elif is_weekend == True and cigars >= 40:
        print("True")
    else:
        print("False")


cigar_party(30, False)
cigar_party(50, False)
cigar_party(70, True)