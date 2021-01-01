import tools
import config.the_three_kingdoms # 导入配置
import config.water_margin
import config.journey_to_the_west

# tools.count_words('data/the_three_kingdoms.txt', config.the_three_kingdoms, True, 'output/the_three_kingdoms.csv')
# tools.count_words('data/water_margin.txt', config.water_margin, True, 'output/water_margin.csv')
tools.count_words('data/journey_to_the_west.txt', config.journey_to_the_west, True, 'output/journey_to_the_west.csv')
