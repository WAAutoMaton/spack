# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install wa-pnetcdf
#
# You can edit this file again by typing:
#
#     spack edit wa-pnetcdf
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class WaPnetcdf(AutotoolsPackage):
    """
    A Parallel I/O Library for NetCDF File Access
    Packaged by WA
    """

    homepage = "https://parallel-netcdf.github.io/"
    url = "https://parallel-netcdf.github.io/Release/pnetcdf-1.12.3.tar.gz"

    maintainers("WAAutoMaton")

    # FIXME: Add the SPDX identifier of the project's license below.
    #license("UNKNOWN")

    version("1.12.3", sha256="439e359d09bb93d0e58a6e3f928f39c2eae965b6c97f64e67cd42220d6034f77")
    
    variant("mpi-path",values=str,default="USE-DEFAULT")
    variant("with-nvhpc",default=False)

    depends_on("mpi")
    depends_on("nvhpc",when="+with-nvhpc")
    depends_on("zlib")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool",  type="build")
    depends_on("m4")

    def configure_args(self):
        nvhpc = bool(self.spec.variants['with-nvhpc'].value)
        if nvhpc:
            mpi_path = self.spec['nvhpc'].prefix+'/Linux_x86_64/23.9/comm_libs/mpi/bin/'
        else:
            mpi_path = self.spec['mpi'].prefix
        print(mpi_path)
        args = ["--enable-shared", f"--with-mpi={mpi_path}"]
        return args

    def setup_build_environment(self, env):
        #env.set('C_INCLUDE_PATH', self.spec['nvhpc'].prefix+'/Linux_x86_64/23.9/compilers/include/')
        #env.set('CPLUS_INCLUDE_PATH', self.spec['nvhpc'].prefix+'/Linux_x86_64/23.9/compilers/include/')
        env.set('MPICC','mpicc')
        env.set('MPICXX','mpicxx')
        env.set('MPIF77','mpif77')
        env.set('MPIF90','mpif90')
        env.set('MPIFORT','mpifort')

    def setup_run_environment(self, env):
        env.prepend_path('LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('CPATH', self.prefix.include)
        env.set('PNETCDF',self.prefix)
        env.prepend_path('C_INCLUDE_PATH', self.prefix.include)
        env.prepend_path('CPLUS_INCLUDE_PATH', self.prefix.include)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.prepend_path('LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('LD_LIBRARY_PATH', self.prefix.lib)
        env.prepend_path('CPATH', self.prefix.include)
        env.set('PNETCDF',self.prefix)
        env.prepend_path('C_INCLUDE_PATH', self.prefix.include)
        env.prepend_path('CPLUS_INCLUDE_PATH', self.prefix.include)
