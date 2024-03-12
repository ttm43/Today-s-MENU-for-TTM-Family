from collections import defaultdict
import numpy as np

# 假设的菜品口味特征
dish_flavors = {
    "宫保鸡丁": ["辣", "麻"],
    "酸辣土豆丝": ["酸", "辣"],
    "牛肉汤": ["清淡"],
    "清蒸鱼": ["清淡"],
}

# 创建标签-索引映射
index = {tag: idx for idx, tag in enumerate(set(tag for tags in dish_flavors.values() for tag in tags))}

# 向量化口味标签
def vectorize_tags(tags, index):
    vec = np.zeros(len(index))
    for tag in tags:
        vec[index[tag]] = 1
    return vec

# 计算余弦相似度
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 向量化示例菜品的口味标签
vec_宫保鸡丁 = vectorize_tags(dish_flavors["宫保鸡丁"], index)
vec_酸辣土豆丝 = vectorize_tags(dish_flavors["酸辣土豆丝"], index)

# 计算相似度
similarity = cosine_similarity(vec_宫保鸡丁, vec_酸辣土豆丝)
print(f"余弦相似度：{similarity}")
