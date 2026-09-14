import json

# 讀取 raw.txt
raw_data = []
with open('data/raw.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()[1:] # 跳過標頭
    for line in lines:
        year, pop = line.strip().split(',')
        raw_data.append({'year': int(year), 'pop': float(pop)})

# 計算統計值
pops = [d['pop'] for d in raw_data]
avg_pop = sum(pops) / len(pops)

# 計算 CAGR (2024 到 2100)
start_pop = raw_data[0]['pop']
end_pop = raw_data[-1]['pop']
num_years = raw_data[-1]['year'] - raw_data[0]['year']
cagr = ((end_pop / start_pop) ** (1 / num_years) - 1) * 100

# 計算各階段成長率
growth_rates = {}
for i in range(1, len(raw_data)):
    prev = raw_data[i-1]['pop']
    curr = raw_data[i]['pop']
    rate = ((curr - prev) / prev) * 100
    growth_rates[f"{raw_data[i-1]['year']}-{raw_data[i]['year']}"] = round(rate, 2)

result = {
    "timeline": raw_data,
    "metrics": {
        "average_population_billions": round(avg_pop, 2),
        "overall_cagr_percent": round(cagr, 2),
        "period_growth_rates": growth_rates
    }
}

with open('data/cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("Data successfully cleaned and saved to data/cleaned.json")
