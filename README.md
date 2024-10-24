# JAX-NB: Long-range Interactions Implemented by JAX

This is a JAX implementation of Polarizable Charge Equilibrium (PQEq) and DFT-D3 diserpsion correction.

## Installation

```bash
pip install .
```

## Advanced

For NVIDIA-GPU acceleration (or other platforms), you should compile the JAX library with CUDA support. Please refer to the [JAX installation guide](https://jax.readthedocs.io/en/latest/installation.html#installation).

```bash
pip install -U "jax[cuda12]"
pip install jax-md
pip install .
```

## Code test environment
- Python 3.9
- JAX 0.4.20
- JAX-MD 0.2.8
- NumPy 1.23.4

## Reference

If you use this repository, please cite the following [preprint](https://doi.org/10.48550/arXiv.2410.13820):
```
@article{gao2024enhancing,
  title={Enhancing universal machine learning potentials with polarizable long-range interactions},
  author={Gao, Rongzhi and Yam, ChiYung and Mao, Jianjun and Chen, Shuguang and Chen, GuanHua and Hu, Ziyang},
  journal={arXiv preprint arXiv:2410.13820},
  year={2024}
}
```