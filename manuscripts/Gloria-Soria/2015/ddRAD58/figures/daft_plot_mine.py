#daft drawing for SMS example
import matplotlib.pyplot as plt

try:
    import daft
except ImportError:
    print "python library Daft required."
    

pgm = daft.PGM([9.7, 5], origin=[0, 0], grid_unit=1)

xadj = 1.8

pgm.add_node(daft.Node("alpha_uniform", r"$\mathcal{U}(0.01,10)_{\alpha}$", x=0.5+xadj, y=4, scale=1.05, aspect=3,
observed=False))
pgm.add_node(daft.Node("beta_uniform", r"$\mathcal{U}(0.01,10)_{\beta}$", x=5.5+xadj, y=4, scale=1.05, aspect=3,
observed=False))

pgm.add_node(daft.Node("alpha", r"$\alpha$", x=2+xadj, y=2.5, scale=1, aspect=1, observed=False))
pgm.add_node(daft.Node("beta", r"$\beta$", x=4+xadj, y=2.5, scale=1, aspect=1, observed=False))

# observed data fit to Beta
pgm.add_node(daft.Node("obs", r"$\mathrm{Beta}(\alpha,\beta)_{\mathrm{obs}}$", x=3+xadj, y=1, scale=1, aspect=3,
                       observed=True))




pgm.add_edge("beta", "obs")
pgm.add_edge("alpha", "obs")
pgm.add_edge("alpha_uniform", "alpha")
pgm.add_edge("beta_uniform", "beta")

pgm.render()
plt.savefig("bin_MAP_model.png")
plt.savefig("bin_MAP_model.pdf")
