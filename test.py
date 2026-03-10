def simulate(
    house_price,
    youth_ratio,
    treasury_rate,
    investor_amount,
    sale_price,
    years,
    insurance_rate,
    eviction_months,
    issuance_fee_rate,
    management_fee_rate,
    sale_fee_rate
):

    investor_ratio = 1 - youth_ratio

    youth_equity = house_price * youth_ratio
    investor_equity = house_price * investor_ratio

    annual_interest = investor_equity * treasury_rate
    monthly_interest = annual_interest / 12

    youth_balance = youth_equity
    months = 0

    # 청년 자본 소진 시점
    while youth_balance > 0:
        youth_balance -= monthly_interest
        months += 1

    years_survivable = months / 12

    investor_share = investor_amount / investor_equity

    quarterly_dividend_total = annual_interest / 4

    # 보험
    insurance_fee = quarterly_dividend_total * insurance_rate
    dividend_after_insurance = quarterly_dividend_total - insurance_fee

    investor_quarterly_dividend = dividend_after_insurance * investor_share

    total_quarters = years * 4
    investor_total_dividend = investor_quarterly_dividend * total_quarters

    # 매각 차익
    capital_gain = sale_price - house_price

    investor_gain_total = capital_gain * investor_ratio
    youth_gain = capital_gain * youth_ratio

    investor_sale_gain = investor_gain_total * investor_share

    # 보험 풀
    insurance_pool = insurance_fee * total_quarters

    lawsuit_quarters = eviction_months / 3
    lost_dividend = quarterly_dividend_total * lawsuit_quarters

    insurance_cover = min(insurance_pool, lost_dividend)

    # 회사 수익 모델

    issuance_fee = investor_equity * issuance_fee_rate

    management_fee = (quarterly_dividend_total * total_quarters) * management_fee_rate

    sale_fee = sale_price * sale_fee_rate

    company_total_revenue = issuance_fee + management_fee + sale_fee + (insurance_pool - insurance_cover)

    print("\n===== 청년 시뮬레이션 =====")
    print(f"집 가격: {house_price:,.0f} 원")
    print(f"청년 초기 투자금: {youth_equity:,.0f} 원")
    print(f"월 이자 부담: {monthly_interest:,.0f} 원")
    print(f"이자 못낼 경우 버틸 수 있는 기간: {months} 개월 ({years_survivable:.2f} 년)")
    print(f"{years}년 후 매각 시 청년 수익: {youth_gain:,.0f} 원")

    print("\n===== 투자자 시뮬레이션 =====")
    print(f"투자 금액: {investor_amount:,.0f} 원")
    print(f"분기 배당: {investor_quarterly_dividend:,.0f} 원")
    print(f"{years}년 총 배당: {investor_total_dividend:,.0f} 원")
    print(f"매각 수익: {investor_sale_gain:,.0f} 원")
    print(f"총 수익: {(investor_total_dividend + investor_sale_gain):,.0f} 원")

    print("\n===== 보험 시스템 =====")
    print(f"보험 적립금: {insurance_pool:,.0f} 원")
    print(f"소송 손실: {lost_dividend:,.0f} 원")
    print(f"보험 보전: {insurance_cover:,.0f} 원")
    print(f"보험 잔여 이익: {(insurance_pool - insurance_cover):,.0f} 원")

    print("\n===== 회사 수익 =====")
    print(f"토큰 발행 수수료: {issuance_fee:,.0f} 원")
    print(f"운용 수수료: {management_fee:,.0f} 원")
    print(f"매각 수수료: {sale_fee:,.0f} 원")
    print(f"보험 수익: {(insurance_pool - insurance_cover):,.0f} 원")
    print(f"회사 총 수익: {company_total_revenue:,.0f} 원")


if __name__ == "__main__":

    print("청년주택 토큰화 시뮬레이터\n")

    house_price = float(input("집 가격: "))
    youth_ratio = float(input("청년 지분 비율 (예 0.1): "))
    treasury_rate = float(input("국채 금리 (예 0.04): "))
    investor_amount = float(input("투자 금액: "))
    sale_price = float(input("N년 후 매각 가격: "))
    years = int(input("보유 기간 (년): "))
    insurance_rate = float(input("보험료 비율 (예 0.05): "))
    eviction_months = int(input("퇴거 소송 기간 (개월): "))

    issuance_fee_rate = float(input("토큰 발행 수수료율 (예 0.005): "))
    management_fee_rate = float(input("운용 수수료율 (예 0.1): "))
    sale_fee_rate = float(input("매각 수수료율 (예 0.01): "))

    simulate(
        house_price,
        youth_ratio,
        treasury_rate,
        investor_amount,
        sale_price,
        years,
        insurance_rate,
        eviction_months,
        issuance_fee_rate,
        management_fee_rate,
        sale_fee_rate
    )