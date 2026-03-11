def simulate_simple(
    house_price,
    youth_ratio,
    monthly_usage_fee,
    investor_amount,
    sale_price,
    years,
    issuance_fee_rate,
    management_fee_rate
):
    investor_ratio = 1 - youth_ratio
    youth_equity = house_price * youth_ratio
    investor_equity = house_price * investor_ratio
    if investor_ratio <= 0:
        print("오류: 청년 지분 비율은 0보다 크고 1보다 작아야 합니다. 예: 0.1")
        return
    if investor_amount > investor_equity:
        print("오류: 투자 금액이 전체 투자자 지분 금액보다 클 수 없습니다.")
        return
    investor_share = investor_amount / investor_equity
    months = years * 12
    quarters = years * 4
    if monthly_usage_fee > 0:
        survivable_months = youth_equity / monthly_usage_fee
        survivable_years = survivable_months / 12
    else:
        survivable_months = float("inf")
        survivable_years = float("inf")
    quarterly_dividend_total = monthly_usage_fee * 3
    investor_quarterly_dividend = quarterly_dividend_total * investor_share
    investor_total_dividend = investor_quarterly_dividend * quarters
    capital_gain = sale_price - house_price
    youth_sale_gain = capital_gain * youth_ratio
    investor_gain_total = capital_gain * investor_ratio
    investor_sale_gain = investor_gain_total * investor_share
    investor_total_profit = investor_total_dividend + investor_sale_gain
    investor_total_cash = investor_amount + investor_total_profit
    if investor_amount > 0 and years > 0:
        investor_total_return_rate = (investor_total_profit / investor_amount) * 100
        investor_annual_return_rate = ((investor_total_cash / investor_amount) ** (1 / years) - 1) * 100
    else:
        investor_total_return_rate = 0
        investor_annual_return_rate = 0
    issuance_fee = investor_amount * issuance_fee_rate
    total_usage_fee = monthly_usage_fee * months
    management_fee = total_usage_fee * management_fee_rate
    company_total_revenue = issuance_fee + management_fee
    print("\n===== 청년 시뮬레이션 =====")
    print(f"집 가격: {house_price:,.0f} 원")
    print(f"청년 초기 투자금: {youth_equity:,.0f} 원")
    print(f"청년 지분 비율: {youth_ratio:.0%}")
    print(f"월 임대 사용료: {monthly_usage_fee:,.0f} 원")
    if survivable_months == float("inf"):
        print("청년 자본으로 버틸 수 있는 기간: 무한대")
    else:
        print(f"청년 자본으로 버틸 수 있는 기간: {survivable_months:,.1f} 개월 ({survivable_years:.2f} 년)")
    print(f"{years}년 후 매각 시 청년 매각차익: {youth_sale_gain:,.0f} 원")
    print("\n===== 투자자 시뮬레이션 =====")
    print(f"투자자 전체 지분 가치: {investor_equity:,.0f} 원")
    print(f"투자 금액: {investor_amount:,.0f} 원")
    print(f"전체 투자자 지분 중 보유 비율: {investor_share:.2%}")
    print(f"분기 배당: {investor_quarterly_dividend:,.0f} 원")
    print(f"{years}년 총 배당: {investor_total_dividend:,.0f} 원")
    print(f"매각 수익: {investor_sale_gain:,.0f} 원")
    print(f"총 수익: {investor_total_profit:,.0f} 원")
    print(f"총 수익률: {investor_total_return_rate:.2f}%")
    print(f"연환산 수익률: {investor_annual_return_rate:.2f}%")
    print("\n===== 회사 수익 =====")
    print(f"토큰 발행 수수료: {issuance_fee:,.0f} 원")
    print(f"운용 수수료: {management_fee:,.0f} 원")
    print(f"회사 총 수익: {company_total_revenue:,.0f} 원")
print("청년주택 토큰화 시뮬레이터\n")
house_price = float(input("1. 집 가격: "))
youth_ratio = float(input("2. 청년 지분 비율 (예: 0.1): "))
monthly_usage_fee = float(input("3. 청년의 월 임대 사용료: "))
investor_amount = float(input("4. 투자자의 투자 금액: "))
sale_price = float(input("5. N년 후 매각 가격: "))
years = int(input("6. 보유 기간 (년): "))
issuance_fee_rate = float(input("7. 토큰 발행 수수료율 (예: 0.05): "))
management_fee_rate = float(input("8. 운용 수수료율 (예: 0.1): "))
simulate_simple(
    house_price,
    youth_ratio,
    monthly_usage_fee,
    investor_amount,
    sale_price,
    years,
    issuance_fee_rate,
    management_fee_rate
)