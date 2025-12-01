<h1>JAX-NB</h1>

![vistors](https://visitor-badge.laobi.icu/badge?page_id=reaxnet.jax-nb&right_color=green) 
<a href='https://arxiv.org/abs/2410.13820'><img src='https://img.shields.io/badge/arXiv-2403.13820-blue'></a>

The JAX implementation of [Polarizable Charge Equilibrium (PQEq) method](https://doi.org/10.1063/1.4978891) and [DFT-D3 diserpsion correction](https://doi.org/10.1063/1.3382344).
## Installation

### Easy install
```bash
pip install git+https://github.com/reaxnet/jax-nb.git
```

### Advanced install (recommend)

For NVIDIA-GPU acceleration, you should compile the JAX library with CUDA support. Please refer to the [JAX installation guide](https://jax.readthedocs.io/en/latest/installation.html#installation) for other platforms acceleration.

```bash
pip install -U "jax[cuda12]"
pip install jax-md
pip install git+https://github.com/reaxnet/jax-nb.git
```

## Usage
Please refer to [example/basic.ipynb](./example/basic.ipynb). It details usage, output and time cost.

## Code test environment

### Python Dependencies
- Python 3.9
- JAX 0.4.20
- JAX-MD 0.2.8
- NumPy 1.23.4

### OS Requirements
This package is supported for macOS and Linux. The code has tested on:
- Ubuntu 22.04.4 LTS
- MacOS 14.7

## Reference

If you use this repository, please cite the following [paper](https://www.nature.com/articles/s41467-025-65496-3):
```bib
@article{reaxnet,
  title={A foundation machine learning potential with polarizable long-range interactions for materials modelling},
  author={Gao, Rongzhi and Yam, ChiYung and Mao, Jianjun and Chen, Shuguang and Chen, GuanHua and Hu, Ziyang},
  journal={Nature Communications},
  year={2025},
  volume={16},
  pages={10484},
}
```
