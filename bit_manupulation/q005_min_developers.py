"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/minimum-number-of-software-developers-official/ojquestion?__cf_chl_jschl_tk__=073ba81643d8cb00f9c66dff3a40be76f14ef459-1616613336-0-AQmDlmW8ITJqNN57VCHpOCcgqm479CoOgvKMu2f8PCIFMdesnDkkkWCxoxTs9s0rSmBJhmzmN7r6dB1BrXFxPTKINIHu3LoZVUSSMk35IMfnGoJHdMR4QwkejqVMryQyg-pBUxO_8khmal1wVms_QV8_pWiOvBBFLiRt_gpsHLLYqhKNMzt08TSjVQnZWguH9E589CC7hq4EZdItDgBOw9T8XXK0kCYklcA7P3lNhBqnTMjAxa1TK3_B6QF2bwr7IHO7HBQPpt92myl_ghoriW9NzQXLL_DiJheC-l5Cz0tJBVUG1LWEgZ8-pqaA-dKGtxP6C9ksgNNPjuj9lCbyXPQ4J5nmQego1IjqXJ9KW2_KRZIjFwX-H8Wl9wt1xviAouBdMpJ3BDGp-iP-87oY2ZWea6S5jsKdVaxkXNQOJfp5iW8zgRAKEl9dx8oIdJl6iSpxOu9YG2seGfIOtovCl_JgYjOqUukMZY1or1xoIvPOwsh5EFwAMDmQt_SR5KndCg

"""


def solve(
        arr, total_skills,
        current_person, one_solution,
        or_skills):
    if current_person == len(arr):
        if or_skills == (1 << total_skills) - 1:
            global participants
            if len(one_solution) == 0 or len(one_solution) < len(participants):
                participants = one_solution.copy()
        return

    solve(
        arr,
        total_skills,
        current_person + 1,
        one_solution,
        or_skills)

    one_solution.append(current_person)
    solve(
        arr,
        total_skills,
        current_person + 1,
        one_solution,
        or_skills | arr[current_person])
    one_solution.pop()


if __name__ == "__main__":
    N = int(input())
    skills = input().split()

    skills_dict = {}
    for idx, value in enumerate(skills):
        skills_dict[value] = idx
    all_skill_mask = (1 << N) - 1

    M = int(input())
    sde = []
    for _ in range(M):
        t = int(input())
        skill_mask = 0
        for _ in range(t):
            skill = input()
            skill_mask |= 1 << skills_dict[skill]
        sde.append(skill_mask)

    participants = [0]*M
    solve(sde, N, 0, [], 0)
    print(participants)
