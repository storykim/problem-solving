n, m = map(int,input().split())
truth = list(map(int, input().split()))
truth = set(truth[1:])

parties = [ tuple(map(int, input().split()))[1:] for _ in range(m)]

updated = True
while updated:
    updated = False
    for party in parties[:]:
        for person in party:
            if person in truth:
                for p in party:
                    truth.add(p)

                parties.remove(party)
                updated = True
                break

print(len(parties))
