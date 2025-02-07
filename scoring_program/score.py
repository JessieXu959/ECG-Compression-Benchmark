import os
import numpy as np
import scipy.io
import json

def main():
    # 用户结果路径
    user_output_dir = "/input"
    # 参考数据路径（如果使用 reference_data）
    truth_dir = "/truth"

    # 读取用户结果
    compressed = np.load(os.path.join(user_output_dir, "compressed_signal.npy"))
    reconstructed = np.load(os.path.join(user_output_dir, "reconstructed_signal.npy"))

    # 读取参考数据（例如真实 ECG 信号）
    truth_data = scipy.io.loadmat(os.path.join(truth_dir, "test_truth.mat"))
    original_signal = truth_data["ecg"].flatten()

    # 计算指标
    compression_ratio = len(original_signal) / len(compressed)
    mse = np.mean((original_signal - reconstructed) ** 2)

    # 生成评分文件
    with open("/output/scores.json", "w") as f:
        json.dump({
            "compression_ratio": compression_ratio,
            "mse": mse
        }, f)

if __name__ == "__main__":
    main()