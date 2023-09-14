# 게임 전투 공식 예시
# 1. 명중률 확률을 먼저 계산해 맞췄는지 판단한다.
# 2. 데미지는 내 공격력이 상대방의 "방어력"보다 높아야 한다.
# 3. 방어력 - 공격력은 최종 데미지가 된다.
# 4. 적의 HP는 데미지보다 많아야 차감이 이루어지고, 아니면 "사망" 처리된다.

# - 반복문을 이용해서 체력이 100인 몬스터를 랜덤하게 변하는 명중률에 의해
# - 공격을 하고 체력이 0이하가 되면 사망하는 전투를 구현 해 보자.
# - 몇 번 반복해야 할지 알 수 있을까?

# [ 예시 ]
# 공격에 성공 하였습니다.
# 50의 체력이 남았습니다.
# 35 명중률
# 공격에 실패하였습니다.

import random

MonsterHP = 100
MonsterDef = 50
Damage = 60
Accuracy = 50

# 4. 적의 HP는 데미지보다 많아야 차감이 이루어지고, 아니면 "사망" 처리된다.
while MonsterHP > 0:

    # 1. 명중률 확률을 먼저 계산해 맞췄는지 판단한다.
    Accuracy = random.randint(0, 100)
    if Accuracy > 50:
        print("\n공격 명중 : %d" %Accuracy)

        # 2. 데미지는 내 공격력이 상대방의 "방어력"보다 높아야 한다.
        if Damage > MonsterDef:

            # 3. 방어력 - 공격력은 최종 데미지가 된다.
            MonsterHP -= (Damage - MonsterDef)
            print("대미지 : %d" %(Damage - MonsterDef))
            print("몬스터 체력 : %d\n" %MonsterHP)
    else:
        print("공격 실패 : %d" %Accuracy)

print("\n몬스터 사망")