import tools
import config.the_three_kingdoms # 导入配置
import config.water_margin

# tools.countWords('data/the_three_kingdoms.txt', config.the_three_kingdoms, True, 'output/the_three_kingdoms.csv')
tools.countWords('data/water_margin.txt', config.water_margin, True, 'output/water_margin.csv')