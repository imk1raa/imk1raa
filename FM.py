import hashlib
import numpy as np

def hash_to_binary(x):
    h = hashlib.sha1(x.encode()).hexdigest()
    h_bin = bin(int(h, 16))[2:].zfill(160)  # בדיוק 160 ביט
    return h, h_bin

def rho(binary_string):
    return binary_string[::-1].find('1')

def flajolet_martin(stream):
    R = 0
    rows = []

    print("\n--- פירוט כל איבר בזרם ---")
    for x in stream:
        h_hex, h_bin = hash_to_binary(x)
        r = rho(h_bin)
        R = max(R, r)

        print(f"\nאיבר: {x}")
        print(f"SHA-1: {h_hex}")
        print(f"בינארי: {h_bin}")
        print(f"ρ(x) = {r}")

        rows.append([x, h_hex, h_bin[:60] + "...", r])  # מקצר בינארי להצגה

    estimate = 2 ** R

    print("\n\n--- טבלה מסכמת ---")
    print(f"{'איבר':<15} | {'SHA-1':<40} | {'Hash בינארי (חלקי)':<65} | {'ρ(x)':<5}")
    print("-" * 140)
    for row in rows:
        print(f"{row[0]:<15} | {row[1]:<40} | {row[2]:<65} | {row[3]:<5}")

    print(f"\n>>> הערכת מספר הערכים הייחודיים: 2^{R} = {estimate}")
    return estimate

# דוגמה לזרם
stream = ['192.168.1.4', '192.168.1.2', '192.168.1.2']
flajolet_martin(stream)