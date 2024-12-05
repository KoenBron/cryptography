import string
import numpy as np
from math import gcd, ceil

N_MIN_REPETITIONS = 3

test_cypher= """Auge y bxwfcxc xl wrpk shbrt eiwemsttrnwr, mg kj awtrtgu ztyseg zr xl wrpk. Rwx
qrvyms hj pjrlvbrt vvvi bw pccjtw e pquc dk e pkgftk. Xug tfpgkrf kcmm mf erjaxh
pkgftkxrzk. Rwx guceet fexgj rwx qrujyvx lntu rd kinf. Jmbxsag nfd peavj rd kinf
zr bnwg eyyczi vv syrd se fvagrtg. Jfu ih guceet bx octi xl e fgtptm. Fbvy rwx
trtjmc mlnv jccww gjv ktlwniv ycw xug flt mlnv xcil mg uymjeh xpfu iai fgtptm ana
km raeaiv gi, uyg qkftk trqgjt llbwcb chx og rzax xb. Ukssrmai kft vmcjvpixbg vf
bxlgbxvp iai fgtptm mf erjaxh ptpnitrnnpqxl.
Hvhwcgxrg vpntl ss eiwemsttrnwr gnp sc ttwvgi mg aeefvp ih yfg rls vea jzbt mlr
uvagxx zgjqpzi ogkrtk se yfphx. Gvrycgl yfg r itr auktf xl e fgtptm xuck fxwif vyc
hxgegk ktlwnivq. Iai ptpnihkecgfxv qrvyms girf emi ui fgtptm. Zntzmjl trqgjt vea
wjc iai fcdc bxxuqu zjm hvhwcgxrg mvwh, ls gjvw rtraqk ptth rctf dmlrt’j ktlwnivq.
Hbrpg kft Verurp rbtugi fpl sanp yh feaa bcnl ef vyc cnqogi mu eigvvph br gjv
yailndvr, xm mf grqxec ptrazxh oa kpnbrt ccj iai xgpq. Rbtugiq iaeg ccjdp fvncgdgw
bh bcnl eeg tppvorf sw bhvr efkeeik ovrwhhf."""

cypher1 = """Ytgj,twstyytgj,ymfynxymjvzjxynts:Bmjymjw’ynxstgqjwnsymjrnsiyt
 xzkkjwYmjxqnslxfsi fwwtbxtktzywfljtzxktwyzsj,Twytyfpj fwrxflfnsxyf
 xjftkywtzgqjxFsigdtuutxnsl jsiymjr.Ytinj—ytxqjju,Strtwj; fsigdfxqjju
 ytxfdbj jsiYmjmjfwy-fhmj fsiymjymtzxfsi sfyzwfqxmthpxYmfykqjxmnx
 mjnwyt: ’ynxfhtsxzrrfyntsIjatzyqdytgjbnxm’i."""

cypher2 = """Ftkins Xpk Wvzu; llna eeryc Tdgq nyx Btsl? W ldvfomx Flvs! Wpzr tizoc, Xcs
hycyiuq! Xywct mauiz Nizbv X ez meqz xf ycda; Goma Flp tdgxu-zxzqedwcv
Pvmi jqazzstvf ti.
Buqv ob X, pnfmvs hvgdaegl xpq affas, Qnki umrztthx bu iidxy hd hpnf qizozbs!
Csg vrm aj rza ilrzi emviwdgw ehroqh wcg hxepjm Qwtoetxu kiifl; kvdj wuhpb
mpfbt hyecmdq.
Xysgtjbyi afeer je! avu jwd xymhtps yivaae, Qdcuhlv btc wcth, iaqsg flv ktppgo
jqxpvr gteyt, Fg Yi kvtn eel etdirrn dzrygwyi, Ss iwsh alm aykkpgh phyaq,
pvti-weakil arv. Rgdrn hrl Nlˆıjvbp eak Nikeufpiln, Rezze, rbs ppy alm axysg
leeymwdw ysgt, Eel wtmme pn Bi. Qlwbdsp hwtq slezxijgan. Jvnlb! flfi hweya
gzgwy hwn vvcete me hwt jvlpl.
Eeexpne fhml: Temwcv lrhvl flvgt lsekw wr Ovgwpzn, oi ets nspgigo e lueusb,
lmgo nwurvr eppzz, ucmozbv prq wvwexioixrt omueict, heexl eomme hd Zvvzlvm, wkobbiepro imkv utee, jeafmeu sdaa oma rets."""

english_frequencies = {
    'a': 0.082,
    'b': 0.015,
    'c': 0.028,
    'd': 0.042,
    'e': 0.127,
    'f': 0.022,
    'g': 0.020,
    'h': 0.061,
    'i': 0.070,
    'j': 0.001,
    'k': 0.008,
    'l': 0.040,
    'm': 0.024,
    'n': 0.067,
    'o': 0.075,
    'p': 0.019,
    'q': 0.001,
    'r': 0.060,
    's': 0.063,
    't': 0.090,
    'u': 0.028,
    'v': 0.010,
    'w': 0.024,
    'x': 0.001,
    'y': 0.020,
    'z': 0.001
}

# Create a lookup table for a given shiftkey
def create_shift_dict(shift_key):
    abc = string.ascii_lowercase
    shifted = abc[shift_key:] + abc[:shift_key]
    return_dict = {}
    for a,b in zip(abc, shifted):
        return_dict[a] = b
    return return_dict

def shift_cypher(shift_dict, cypher):
    shifted_cypher = []
    for char in cypher:
        shifted_cypher.append(shift_dict.get(char.lower(), char))
    return shifted_cypher

def print_as_string(array):
    for char in array:
        print(char, end="")
    print('\n')
        
def shift_solver(cypher, shift_key):
    shift_dict = create_shift_dict(shift_key)
    shifted_cypher = shift_cypher(shift_dict=shift_dict, cypher=cypher.lower())

    # Clear the shifted cypher of non alphabetic characters
    filtered_cypher = [char for char in shifted_cypher if char in string.ascii_lowercase]
    letters, counts = np.unique(np.array(filtered_cypher), return_counts=True)

    # Get the percentages
    cypher_frequencies = {}

    # np.unique put the letters in alphabetical order
    for letter, count in zip(letters, counts):
        cypher_frequencies[letter] = count/len(filtered_cypher)
    
    # Compute the statistical distance
    st_dist = 0
    for key in cypher_frequencies.keys():
        st_dist += abs(english_frequencies[key] - cypher_frequencies[key])
    
    return st_dist, shifted_cypher

def solve_cypher1():
    min_dist, min_result = shift_solver(cypher=cypher1, shift_key=0)
    key = 0
    # Go through all shift key possibilities
    for i in range(1,26):
        dist, result = shift_solver(cypher=cypher1, shift_key=i)
        if dist < min_dist:
            min_dist, min_result, key = dist, result, i
    print("Key: ", key)
    print("Solution: ", end="")
    print_as_string(min_result)

def solve_test_cypher():
    min_dist, min_result = shift_solver(cypher=test_cypher, shift_key=0)
    key = 0
    # Go through all shift key possibilities
    for i in range(1,26):
        dist, result = shift_solver(cypher=test_cypher, shift_key=i)
        if dist < min_dist:
            min_dist, min_result, key = dist, result, i
    print("Key: ", 26-key)
    print("Decrypted: ", end="")
    print_as_string(min_result)

# Helper function to create a list of all positions of substr in 
def find_positions(cypher, substr, substr_length):
    positions = []
    index = cypher.find(substr)
    while index != -1:
        positions.append(index)
        index = cypher.find(substr, index+substr_length)
    return positions
        
# Search all 2 and 3 letter substrings and get their positions
def find_substring_positions(filtered_cypher):
    substr_lengths = [3]
    
    # Dictionary to be filled with substrings and a list of positions their occurrences
    positions = {}
    for substr_length in substr_lengths:
        offset = 0

        # Divide the cypher into substrings of lenght substr_length
        while offset + substr_length < len(filtered_cypher):
            substr = filtered_cypher[offset:offset+substr_length]

            # Check if we have already counted this substring and check if the substring occurs frequently enough
            # Note: .count(substr) counts the amount of non overlapping occurrences
            if substr not in positions.keys() and filtered_cypher.count(substr) >= N_MIN_REPETITIONS:
                # Get the positions
                substr_pos = find_positions(cypher=filtered_cypher, substr=substr, substr_length=substr_length)
                positions[substr] = substr_pos

            offset += 1 # Increment loop

    return positions

# Get the most likely keylengths based on the position differences of the repeating segments
def most_likely_keylength(substring_positions):
    distances = []
    for sequence in substring_positions:
        positions = substring_positions[sequence]
        # For each sequence compute the distance between alle elements
        for i in range(len(positions) - 1):
            for j in range(i+1, len(positions)):
                distances.append(abs(positions[i] - positions[j]))

    # Get the lenght by computing the greatest common divider of all distances
    keylength = gcd(*distances)
    return keylength

def compute_distance(cypher, shift):
    # Shift cypher
    base = ord('a')
    shifted_cypher = []
    for letter in cypher:
        shifted_cypher.append(chr((ord(letter) - base + shift)%26 + base))

    # Gather the frequencies of the shift
    unique, counts = np.unique(np.array(shifted_cypher), return_counts=True)
    distance = 0

    # Compute the distance of each letter to the frequencies of the english language
    for letter, count in zip(unique, counts):
        distance += abs(english_frequencies[letter] - count/len(cypher))
    return distance

# Return the optimal shift value based on the statistical difference
def compute_shift_value(filtered_cypher):
    min_dist = compute_distance(filtered_cypher,0)
    key = 0

    for shift in range(1,26):
        distance = compute_distance(filtered_cypher, shift)
        if distance < min_dist:
            min_dist = distance
            key = shift

    return key

def kasinski_attack(cypher):
    # Filter the cypher of non-alphabetic characters
    filtered_cypher = "".join(char for char in cypher.lower() if char in string.ascii_lowercase)

    # Get the keylenght based on the distance between repeating sequences
    substring_positions = find_substring_positions(filtered_cypher=filtered_cypher)
    keylength = most_likely_keylength(substring_positions=substring_positions)

    # Divide the cypher into columns such that each elements is in the same position relative to the keylength
    
    # Array of keylenght size with empty strings to be filled
    columns = ['' for _ in range(keylength)]
    
    # Fill the columns
    for i, char in enumerate(filtered_cypher):
        columns[i % keylength] += char

    # Find the shiftvalue for each column based on the statistical distance between the english letter frequencies
    shift_values = []
    for i in range(len(columns)):
        shift_values.append(compute_shift_value(filtered_cypher=columns[i]))
    
    return shift_values, keylength

def decrypt_vigenere(cypher, shift_values, keylength):
    # Generate shifted lookup tables for each letter in the key
    lookup_table = [create_shift_dict(value) for value in shift_values]
    decrypted = ""
    i = 0
    counter = 0

    # Go through the each encrypted letter and decrypt it
    while i < len(cypher):
        value = lookup_table[counter % keylength].get(cypher[i].lower())
        if value == None:
            decrypted += cypher[i]
        
        else:
            counter += 1
            decrypted += value
        
        i += 1
    
    return decrypted
        
    
def solve_cypher2():
    # Get the key in numerical form
    shift_values, keylength = kasinski_attack(cypher=cypher2)
    print("Keylength: ", keylength)

    # After printing debugging the program it was found that the statistical distance doesn't guess that the value for the fourth
    # letter is accurate. It computes to an 'x' while it is expected to be an 'e' based on the resulting decryption and the fact
    # that an english name was used for as the key which is highly unsecure
    shift_values[3] = 22

    # Get the key in plainwords, i.e. (char + shift_value) % 26
    key = ""
    for value in shift_values:
        key += string.ascii_lowercase[26 - value]
    
    print("Key: ", key)

    print("Decrypted: ", decrypt_vigenere(cypher=cypher2, shift_values=shift_values, keylength=keylength))

def solve_testcypher2():
    # Get the key in numerical form
    shift_values, keylength = kasinski_attack(cypher=test_cypher)
    print(keylength)

    # Get the key in plainwords, i.e. (char + shift_value) % 26
    key = ""
    for value in shift_values:
        key += string.ascii_lowercase[26 - value]
    
    print(key)

    # Lowercase the cypher to work properly
    cypher = test_cypher.lower()

    # Filter the cypher of non-alphabetic characters
    filtered_cypher = "".join(char for char in cypher if char in string.ascii_lowercase)

    print("Decrypted: ", decrypt_vigenere(cypher=filtered_cypher, shift_values=shift_values, keylength=keylength))

if __name__ == "__main__":
    solve_cypher1()
    solve_cypher2()


        

