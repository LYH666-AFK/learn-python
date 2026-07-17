#格式化练习

# 定义需要的变量
name="传智博客"
stock_price=19.99
stock_code="003032"
# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor=1.2
growth_days=7

finally_stock_price=stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司：{name}，股票代码:{stock_code}，当前股价:{stock_price}")
print("每日增长系数是:%.1f，经过%d天的增长后，股价达到了:%.2f"%(stock_price_daily_growth_factor,growth_days,finally_stock_price))


#input练习
print(f"您好:{input("请输入您的姓名：")}，您是尊贵的:{input("请输入您的用户类型：")}用户，欢迎您的光临。")