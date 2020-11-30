# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Coupler(CMakePackage):
    """XGC-GENE coupler."""

    homepage = "https://github.com/wdmapp/wdmapp_coupling"
    # FIXME, there is no tarball, but it still needs a URL, so it's fake
    #url      = "git@github.com:wdmapp/wdmapp_coupling.tar.gz"
    #git      = "git@github.com:wdmapp/wdmapp_coupling.git"
    url      = "git@github.com:Damilare06/wdmapp_coupling.tar.gz"
    git      = "git@github.com:Damilare06/wdmapp_coupling.git"

    maintainers = ['cwsmith','Damilare06','phyboyzhang']

    version('master', branch='master', preferred=True)
    version('develop', branch='develop')
    version('perfstubs', branch='perfstubs')

    variant('perf', default=False,
            description='Turns on the -DPERFSTUBS_USE_TIMERS')


    depends_on('pkgconfig', type='build')
    depends_on('cmake@3.13:', type='build')

    depends_on('adios2@2.5.0:')
    depends_on('kokkos@3.0.0:')
    depends_on('fftw@3.3.8:')
    depends_on('perfstubs', when='+perf')

    def cmake_args(self):
        args = []
        args += ['-DCMAKE_CXX_COMPILER=%s' % self.spec['kokkos'].kokkos_cxx]
        args += ['-DBUILD_TESTING=OFF']
        args += ['-DPERFSTUBS_USE_TIMERS={}'.format('ON' if '+perf' in self.spec else 'OFF')]
        return args

#    def install(self, spec, prefix):
#      options = ["-prefix=%s" % prefix]
#         if '+perfstub' in spec:
#             options.append('-PERFSTUBS_USE_TIMERS')
