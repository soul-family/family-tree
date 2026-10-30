# Hone Family Tree

```mermaid
---
config:
  flowchart:
    defaultRenderer: elk
---
flowchart LR
    %% DATE DISPLAY AND ESTIMATION RULES
    %% All approximate births display c., as requested.
    %% Comments distinguish age-derived, source-approximate and assumption-based dates.
    %% Dates use YYYY Mon DD; unknown components, ranges and quarters are retained.
    %% Completed age A in year Y gives [Y-A-1,Y-A].
    %% Provisional parental ages: 15–60; marriage-only ages: 16–40.
    %% Child [L,U] gives parent [L-60,U-15].
    %% Parent [L,U] gives child [L+15,U+60].
    %% Known marriage year M gives birth [M-40,M-16].
    %% Intersect applicable fallback intervals; never override documentary dates.
    %% CONDITIONAL SPOUSE ESTIMATES: additionally assume both partners married
    %% aged 16–40, giving the other spouse [L-24,U+24] from partner birth [L,U].
    %% This is an additional assumption, not independent evidence of a birth
    %% or a marriage year; do not feed its result back into the input estimate.
    %% Very broad ranges are model envelopes, not documented birth intervals.
    %% Only the second-listed parent points to shared children.
    %% Where only one parent is named, that parent points to the children.
    %% Co-parent links do not assert an undocumented marriage.
    classDef person stroke:#666666;

    %% FOUNDING FAMILY
    1755_william_hone["William Hone<br/>b. 1755 Mar 31; d. 1831"]:::person
    %% Age-derived: death 1833, age 76 => 1756–1757.
    1756_1757_frances_stawell["Frances Maria (Stawell)<br/>b. c. 1756–1757; d. 1833"]:::person
    1755_william_hone ---|married| 1756_1757_frances_stawell
    1780_william_hone["William Hone<br/>b. 1780 Jun 03; d. 1842"]:::person
    1783_joseph_hone["Joseph Hone<br/>b. 1783 Dec 30; d. 1861"]:::person
    1789_judah_hone["Judah Hone<br/>b. 1789 Jun 04"]:::person
    1796_sarah_hone["Sarah Hone<br/>b. 1796 Jun 23"]:::person
    1798_samuel_hone["Samuel Hone<br/>b. 1798 Sep 07"]:::person
    1756_1757_frances_stawell --> 1780_william_hone & 1783_joseph_hone & 1789_judah_hone & 1796_sarah_hone & 1798_samuel_hone

    %% WILLIAM HONE AND SARAH JOHNSON
    1781_sarah_johnson["Sarah (Johnson)<br/>b. 1781 Nov 30; d. 1864"]:::person
    %% Married 1800 Jul 19, St Anne's Soho.
    1780_william_hone ---|1800| 1781_sarah_johnson
    1801_sarah_hone["Sarah (Hone)<br/>b. 1801; d. 1883"]:::person
    1803_fanny_hone["Fanny (Hone)<br/>b. 1803 Apr 05; d. 1883"]:::person
    1805_matilda_hone["Matilda Hone<br/>b. 1805 Jul 26; d. 1884"]:::person
    1807_william_hone["William Hone<br/>b. 1807 Jul 24"]:::person
    1810_alfred_hone["Alfred Hone<br/>b. 1810 Jan 02; d. 1883"]:::person
    %% Assumption-based: father 1780 => 1795–1840;
    %% mother 1781 => 1796–1841; intersection 1796–1840.
    %% No birth-order assumption for these three children.
    1796_1840_john_hone["John Hone<br/>b. c. 1796–1840"]:::person
    1814_emma_hone["Emma (Hone)<br/>b. 1814 Mar 14; d. 1880"]:::person
    1796_1840_charlotte_hone["Charlotte Hone<br/>b. c. 1796–1840"]:::person
    1796_1840_unnamed_hone["Unnamed child<br/>b. c. 1796–1840"]:::person
    %% Charlotte and unnamed child died in infancy; death years unknown.
    1818_rose_hone["Rose Hone<br/>b. 1818 Aug 27; d. 1898"]:::person
    1820_samuel_hone["Samuel Parr Hone<br/>b. 1820 May 09; d. 1870"]:::person
    1822_ellen_hone["Ellen (Hone)<br/>b. 1822 Mar 31; d. 1910"]:::person
    1825_alice_hone["Alice (Hone)<br/>b. 1825 Dec 08"]:::person
    1781_sarah_johnson --> 1801_sarah_hone & 1803_fanny_hone & 1805_matilda_hone & 1807_william_hone & 1810_alfred_hone & 1796_1840_john_hone & 1814_emma_hone & 1796_1840_charlotte_hone & 1796_1840_unnamed_hone & 1818_rose_hone & 1820_samuel_hone & 1822_ellen_hone & 1825_alice_hone

    %% SARAH HONE AND JACOB HENRY BURN
    %% Children 1825,1827,1828 => parent 1768–1810.
    %% Marriage 1822 => 1782–1806; intersection 1782–1806.
    1782_1806_jacob_burn["Jacob Henry Burn<br/>b. c. 1782–1806"]:::person
    %% Married 1822 Jul 13, St Martin-in-the-Fields.
    1801_sarah_hone ---|1822| 1782_1806_jacob_burn
    1825_robert_burn["Robert Burn<br/>b. 1825 Mar 14"]:::person
    1827_henry_burn["Henry Burn<br/>b. 1827 Jan 19"]:::person
    1828_allan_burn["Allan Burn<br/>b. 1828 Oct 27; d. 1883"]:::person
    1782_1806_jacob_burn --> 1825_robert_burn & 1827_henry_burn & 1828_allan_burn

    %% ALLAN BURN AND JOICE MORGAN
    %% Joice born 1833 => each parent estimated 1773–1818.
    1773_1818_john_morgan["John Morgan<br/>b. c. 1773–1818"]:::person
    1773_1818_elizabeth_edwards["Elizabeth (Edwards)<br/>b. c. 1773–1818"]:::person
    1833_joice_morgan["Joice (Morgan)<br/>b. 1833 Jun 17"]:::person
    1773_1818_john_morgan ---|co-parents| 1773_1818_elizabeth_edwards
    1773_1818_elizabeth_edwards --> 1833_joice_morgan
    %% Married 1856 Feb, Taraville, Victoria.
    1828_allan_burn ---|1856| 1833_joice_morgan
    %% All nine children's parentage explicitly confirmed by user.
    %% George's approximate year is source-stated.
    1857_george_burn["George Preece Burn<br/>b. c. 1857"]:::person
    1858_robert_burn["Robert Henry Burn<br/>b. 1858"]:::person
    %% Robert died in infancy; the source does not establish a death year.
    1869_mary_burn["Mary Rose Burn<br/>b. 1869"]:::person
    1862_alice_burn["Alice Charlotte (Burn)<br/>b. 1862 Jun 03"]:::person
    1864_william_burn["William Allan Burn<br/>b. 1864; d. 1865"]:::person
    1866_fanny_burn["Fanny Helina Burn<br/>b. 1866; d. 1872"]:::person
    1868_hilda_burn["Hilda May Burn<br/>b. 1868"]:::person
    1872_katie_burn["Katie Burn<br/>b. 1872"]:::person
    1876_elizabeth_burn["Elizabeth Lillian Burn<br/>b. 1876"]:::person
    1833_joice_morgan --> 1857_george_burn & 1858_robert_burn & 1869_mary_burn & 1862_alice_burn & 1864_william_burn & 1866_fanny_burn & 1868_hilda_burn & 1872_katie_burn & 1876_elizabeth_burn

    %% WILLIAMS FAMILY
    %% David born 1864 => parents estimated 1804–1849.
    1804_1849_evan_williams["Evan Williams<br/>b. c. 1804–1849"]:::person
    1804_1849_besty_jenkins["Besty (Jenkins)<br/>b. c. 1804–1849"]:::person
    1864_david_williams["David Evan Williams<br/>b. 1864 Jul 01; d. 1917"]:::person
    1804_1849_evan_williams ---|co-parents| 1804_1849_besty_jenkins
    1804_1849_besty_jenkins --> 1864_david_williams
    %% Source: married 1833 Nov 08, Middle Creek, Wodonga.
    %% This predates both births; preserve but exclude from estimates.
    1862_alice_burn ---|1833| 1864_david_williams
    1884_may_williams["May Constance (Williams)<br/>b. 1884; d. 1964"]:::person
    1885_arthur_williams["Arthur Allan G. Williams<br/>b. 1885"]:::person
    1887_evan_williams["Evan Jenkins Williams<br/>b. 1887"]:::person
    1864_david_williams --> 1884_may_williams & 1885_arthur_williams & 1887_evan_williams
    %% Each spouse: marriage 1911 => estimated birth 1871–1895.
    1871_1895_maud_oakey["Maud M. (Oakey)<br/>b. c. 1871–1895"]:::person
    1871_1895_hannah_thomas["Hannah (Thomas)<br/>b. c. 1871–1895"]:::person
    1885_arthur_williams ---|1911| 1871_1895_maud_oakey
    1887_evan_williams ---|1911| 1871_1895_hannah_thomas

    %% GRANBERG FAMILY
    %% Frans Edward born 1880 => parents estimated 1820–1865.
    1820_1865_frans_granberg["Frans Granberg<br/>b. c. 1820–1865"]:::person
    1820_1865_maria_erickasen["Maria (Erickasen)<br/>b. c. 1820–1865"]:::person
    1880_frans_granberg["Frans Edward Granberg<br/>b. 1880; d. 1940"]:::person
    1820_1865_frans_granberg ---|co-parents| 1820_1865_maria_erickasen
    1820_1865_maria_erickasen --> 1880_frans_granberg
    %% Married 1910 Dec 28.
    1884_may_williams ---|1910| 1880_frans_granberg
    1911_alice_granberg["Alice M. Granberg<br/>b. 1911"]:::person
    1913_lillian_granberg["Lillian Constance (Granberg)<br/>b. 1913; d. 1998"]:::person
    1916_david_granberg["David Edward Kitchener Granberg<br/>b. 1916 Oct 01; d. 1968"]:::person
    1880_frans_granberg --> 1911_alice_granberg & 1913_lillian_granberg & 1916_david_granberg

    %% BARRETT FAMILY
    1912_richard_barrett["Richard John Barrett<br/>b. 1912 Oct 24; d. 1974"]:::person
    %% Married 1936, Western Australia.
    1913_lillian_granberg ---|1936| 1912_richard_barrett
    %% Children: Lillian 1913 => 1928–1973;
    %% Richard 1912 => 1927–1972; intersection 1928–1972.
    1928_1972_doreen_barrett["Doreen Barrett<br/>b. c. 1928–1972"]:::person
    1928_1972_mervyn_barrett["Mervyn Barrett<br/>b. c. 1928–1972"]:::person
    1928_1972_cheryl_barrett["Cheryl Barrett<br/>b. c. 1928–1972"]:::person
    1928_1972_wayne_barrett["Wayne Barrett<br/>b. c. 1928–1972"]:::person
    1912_richard_barrett --> 1928_1972_doreen_barrett & 1928_1972_mervyn_barrett & 1928_1972_cheryl_barrett & 1928_1972_wayne_barrett

    %% CHERYL GRANT'S FAMILY
    1905_hector_grant["Hector Grant<br/>b. 1905 Jul 23; d. 1986"]:::person
    1909_freda_scot["Freda E. (Scot)<br/>b. 1909; d. 2003"]:::person
    %% Cheryl: Hector 1905 => 1920–1965;
    %% Freda 1909 => 1924–1969; intersection 1924–1965.
    1924_1965_cheryl_grant["Cheryl (Grant)<br/>b. c. 1924–1965"]:::person
    1905_hector_grant ---|co-parents| 1909_freda_scot
    1909_freda_scot --> 1924_1965_cheryl_grant
    1928_1972_mervyn_barrett ---|married| 1924_1965_cheryl_grant
    %% Children depend on estimated parental births:
    %% Mervyn 1928–1972 => 1943–2032;
    %% Cheryl 1924–1965 => 1939–2025; intersection 1943–2025.
    1943_2025_wesley_barrett["Wesley Barrett<br/>b. c. 1943–2025"]:::person
    1943_2025_matthew_barrett["Matthew Barrett<br/>b. c. 1943–2025"]:::person
    1943_2025_melissa_barrett["Melissa (Barrett)<br/>b. c. 1943–2025"]:::person
    1924_1965_cheryl_grant --> 1943_2025_wesley_barrett & 1943_2025_matthew_barrett & 1943_2025_melissa_barrett
    %% Conditional spouse estimates, not source evidence:
    %% Each partner estimated 1943–2025; assuming BOTH partners marry at 16–40
    %% gives spouse [1943-24,2025+24] = 1919–2049.
    %% These wide envelopes depend on the children's estimated births above.
    1919_2049_michelle_otway_melvin["Michelle (Otway-Melvin)<br/>b. c. 1919–2049"]:::person
    1919_2049_lauren_fernandez["Lauren Fernandez<br/>b. c. 1919–2049"]:::person
    1919_2049_lachlan_simson["Lachlan Simson<br/>b. c. 1919–2049"]:::person
    1943_2025_wesley_barrett ---|married| 1919_2049_michelle_otway_melvin
    1943_2025_matthew_barrett ---|married| 1919_2049_lauren_fernandez
    1943_2025_melissa_barrett ---|married| 1919_2049_lachlan_simson

    %% FANNY HONE AND THOMAS HEMSLEY
    %% Thomas born 1798 => parents estimated 1738–1783.
    1738_1783_thomas_hemsley["Thomas Hemsley<br/>b. c. 1738–1783"]:::person
    1738_1783_elizabeth_seaton["Elizabeth (Seaton)<br/>b. c. 1738–1783"]:::person
    1798_thomas_hemsley["Thomas Hemsley<br/>b. 1798 Jun 11"]:::person
    1738_1783_thomas_hemsley ---|co-parents| 1738_1783_elizabeth_seaton
    1738_1783_elizabeth_seaton --> 1798_thomas_hemsley
    %% Married 1826 Apr 29, St Botolph-without-Aldgate.
    1803_fanny_hone ---|1826| 1798_thomas_hemsley
    1827_thomas_hemsley["Thomas Hemsley<br/>b. 1827 Aug 16"]:::person
    1829_william_hemsley["William Hemsley<br/>b. 1829 May 27"]:::person
    1831_fanny_hemsley["Fanny Hemsley<br/>b. 1831 Feb 20"]:::person
    1837_emma_hemsley["Emma (Hemsley)<br/>b. 1837 Mar 14; d. 1899"]:::person
    1844_alfred_hemsley["Alfred Frederick Hemsley<br/>b. 1844 Apr 20; d. 1922"]:::person
    1798_thomas_hemsley --> 1827_thomas_hemsley & 1829_william_hemsley & 1831_fanny_hemsley & 1837_emma_hemsley & 1844_alfred_hemsley
    %% John Walker: marriage 1877 => estimated 1837–1861.
    1837_1861_john_walker["John Walker<br/>b. c. 1837–1861"]:::person
    %% Father depends on son's estimate: [1837-60,1861-15] = 1777–1846.
    %% Source spells father's surname Wallker; retain it.
    1777_1846_john_wallker["John Wallker<br/>b. c. 1777–1846"]:::person
    1777_1846_john_wallker --> 1837_1861_john_walker
    %% Married 1877 Oct 09, Islington Parish Church.
    1837_emma_hemsley ---|1877| 1837_1861_john_walker
    %% Emma Ginder: marriage 1867 => estimated 1827–1851.
    1827_1851_emma_ginder["Emma (Ginder)<br/>b. c. 1827–1851"]:::person
    1844_alfred_hemsley ---|1867| 1827_1851_emma_ginder

    %% THOMAS HEMSLEY AND JESSIE FRANKLYN
    1825_jessie_franklyn["Jessie (Franklyn)<br/>b. 1825 Nov 30; d. 1869"]:::person
    %% Married 1851 Aug 11, Elstree.
    1827_thomas_hemsley ---|1851| 1825_jessie_franklyn
    1851_thomas_hemsley["Thomas Franklyn Hemsley<br/>b. 1851 Dec 09; d. 1916"]:::person
    %% Jessie: age 27 in 1881 => 1853–1854;
    %% age 92 at death in 1945 => 1852–1853. Existing covering range retained.
    1852_1854_jessie_hemsley["Jessie Hemsley<br/>b. c. 1852–1854; d. 1945"]:::person
    %% Henry: age 24 in 1881 => 1856–1857.
    1856_1857_henry_hemsley["Henry Franklyn Hemsley<br/>b. c. 1856–1857"]:::person
    1859_mary_hemsley["Mary (Hemsley)<br/>b. 1859 Mar 08; d. 1946"]:::person
    1861_george_hemsley["George Franklyn Hemsley<br/>b. 1861 Q1; d. 1862"]:::person
    %% Arthur: buried 1865 Jan 28 aged 22 months => approximately 1863.
    1863_arthur_hemsley["Arthur Franklyn Hemsley<br/>b. c. 1863; d. 1865"]:::person
    %% Margaret: age 18 in 1881 => 1862–1863.
    1862_1863_margaret_hemsley["Margaret (Hemsley)<br/>b. c. 1862–1863"]:::person
    1865_kate_hemsley["Kate Hemsley<br/>b. 1865 Jan 17; d. 1930"]:::person
    1867_edith_hemsley["Edith Florence Hemsley<br/>b. 1867 Jul 09"]:::person
    1869_franklyn_hemsley["Franklyn Charles Hemsley<br/>b. 1869 Q4; d. 1869"]:::person
    1825_jessie_franklyn --> 1851_thomas_hemsley & 1852_1854_jessie_hemsley & 1856_1857_henry_hemsley & 1859_mary_hemsley & 1861_george_hemsley & 1863_arthur_hemsley & 1862_1863_margaret_hemsley & 1865_kate_hemsley & 1867_edith_hemsley & 1869_franklyn_hemsley
    %% Henry Wilkinson: marriage 1894 => estimated 1854–1878.
    1854_1878_henry_wilkinson["Henry Elisha Wilkinson<br/>b. c. 1854–1878"]:::person
    %% Married 1894 Sep 04, Oxsted as written in source.
    1859_mary_hemsley ---|1894| 1854_1878_henry_wilkinson

    %% THOMAS FRANKLYN HEMSLEY AND CLARA WILLMOTT THOMAS
    %% Clara: death 1891, age 37 => 1853–1854.
    1853_1854_clara_thomas["Clara Willmott (Thomas)<br/>b. c. 1853–1854; d. 1891"]:::person
    %% Married 1876 Jun 22, Islington.
    1851_thomas_hemsley ---|1876| 1853_1854_clara_thomas
    1877_ethel_hemsley["Ethel Clara Hemsley<br/>b. 1877 Apr 03"]:::person
    1878_violet_hemsley["Violet Mary Hemsley<br/>b. 1878 Apr 02"]:::person
    1879_winifred_hemsley["Winifred Sarah Hemsley<br/>b. 1879 Oct 15"]:::person
    1881_jessie_hemsley["Jessie Maud Hemsley<br/>b. 1881 May 03"]:::person
    1882_gladys_hemsley["Gladys Margaret Hemsley<br/>b. 1882 Nov 26; d. 1883"]:::person
    1884_thomas_hemsley["Thomas Alexis Franklyn Hemsley<br/>b. 1884 Nov 12"]:::person
    1886_robert_hemsley["Robert Harry Hemsley<br/>b. 1886 May 09; d. 1917"]:::person
    1888_doris_hemsley["Doris Evelyn Hemsley<br/>b. 1888 Feb 06"]:::person
    1891_daisy_hemsley["Daisy Rosalie Hemsley<br/>b. 1891 Feb 25"]:::person
    1853_1854_clara_thomas --> 1877_ethel_hemsley & 1878_violet_hemsley & 1879_winifred_hemsley & 1881_jessie_hemsley & 1882_gladys_hemsley & 1884_thomas_hemsley & 1886_robert_hemsley & 1888_doris_hemsley & 1891_daisy_hemsley

    %% HUCKETT FAMILY
    1862_walter_huckett["Walter Huckett<br/>b. 1862 Jan 31"]:::person
    %% Married 1889 Q3, Romford.
    1862_1863_margaret_hemsley ---|1889| 1862_walter_huckett
    1898_hugh_huckett["Hugh Cecil Huckett<br/>b. 1898 Jul 13"]:::person
    1892_arnold_huckett["Arnold Walter Huckett<br/>b. 1892 Feb 27; d. 1915"]:::person
    1894_margaret_huckett["Margaret Christina Huckett<br/>b. 1894 Jul 07"]:::person
    1899_oliver_huckett["Oliver Sharman Huckett<br/>b. 1899 Jul 12; d. 1918"]:::person
    1862_walter_huckett --> 1898_hugh_huckett & 1892_arnold_huckett & 1894_margaret_huckett & 1899_oliver_huckett

    %% ALFRED HONE AND ELIZABETH PREECE
    %% Elizabeth: age 40 in 1851 and 70 in 1881 => 1810–1811.
    1810_1811_elizabeth_preece["Elizabeth (Preece)<br/>b. c. 1810–1811"]:::person
    %% Married 1835 Jun 16, St Pancras Old Church.
    1810_alfred_hone ---|1835| 1810_1811_elizabeth_preece
    1836_alfred_hone["Alfred Hone<br/>b. 1836; d. 1885"]:::person
    %% William: age 3 in 1841 => 1837–1838;
    %% age 12 in 1851 => 1838–1839; common year 1838.
    1838_william_hone["William Hone<br/>b. c. 1838"]:::person
    1842_frances_hone["Frances Elizabeth (Hone)<br/>b. 1842 Q1"]:::person
    1844_nathaniel_hone["Nathaniel Johnson Hone<br/>b. 1844"]:::person
    1810_1811_elizabeth_preece --> 1836_alfred_hone & 1838_william_hone & 1842_frances_hone & 1844_nathaniel_hone

    %% ALFRED HONE AND ANNIE
    %% Annie: age 39 in 1881 => 1841–1842; surname unrecorded.
    1841_1842_annie_unknown["Annie<br/>b. c. 1841–1842"]:::person
    1836_alfred_hone ---|married| 1841_1842_annie_unknown
    %% Edward: ages 14 in 1881 and 34 in 1901 => 1866–1867.
    1866_1867_edward_hone["Edward Hone<br/>b. c. 1866–1867"]:::person
    %% Edith: age 10 in 1881 => 1870–1871.
    1870_1871_edith_hone["Edith Annie (Hone)<br/>b. c. 1870–1871"]:::person
    %% Edgar: age 9 in 1881 => 1871–1872.
    1871_1872_edgar_hone["Edgar Hone<br/>b. c. 1871–1872"]:::person
    %% Lena: age 7 in 1881 => 1873–1874.
    1873_1874_lena_hone["Lena Hone<br/>b. c. 1873–1874"]:::person
    %% Bertie: age 3 in 1881 => 1877–1878.
    1877_1878_bertie_hone["Bertie Hone<br/>b. c. 1877–1878"]:::person
    %% Daisy: age 18 in 1901 => 1882–1883.
    1882_1883_daisy_hone["Daisy V. Hone<br/>b. c. 1882–1883"]:::person
    1841_1842_annie_unknown --> 1866_1867_edward_hone & 1870_1871_edith_hone & 1871_1872_edgar_hone & 1873_1874_lena_hone & 1877_1878_bertie_hone & 1882_1883_daisy_hone

    %% EDWARD HONE AND SARAH THOMPSON
    %% Sarah: age 33 in 1901 => 1867–1868.
    1867_1868_sarah_thompson["Sarah (Thompson)<br/>b. c. 1867–1868"]:::person
    1866_1867_edward_hone ---|married| 1867_1868_sarah_thompson
    1887_fanny_hone["Fanny Amelia (Hone)<br/>b. 1887 Q4"]:::person
    1890_edward_hone["Edward William Hone<br/>b. 1890 Q3"]:::person
    1892_frank_hone["Frank Ernest Hone<br/>b. 1892 Q2"]:::person
    1894_harry_hone["Harry Hone<br/>b. 1894 Q3"]:::person
    %% Harry died aged 77; no independent death year supplied.
    1896_charles_hone["Charles Walter Hone<br/>b. 1896 Q2"]:::person
    1899_george_hone["George Hone<br/>b. 1899 Q3"]:::person
    1901_bertie_hone["Bertie Hone<br/>b. 1901 Q2"]:::person
    1867_1868_sarah_thompson --> 1887_fanny_hone & 1890_edward_hone & 1892_frank_hone & 1894_harry_hone & 1896_charles_hone & 1899_george_hone & 1901_bertie_hone
    %% Conditional spouse estimate from Fanny's documented birth 1887:
    %% both partners marrying aged 16–40 => 1863–1911.
    1863_1911_william_price["William Price<br/>b. c. 1863–1911"]:::person
    1887_fanny_hone ---|married| 1863_1911_william_price
    1894_ada_phillips["Ada Florence (Phillips)<br/>b. 1894 Q4"]:::person
    %% Married 1914 Q1, Birmingham.
    1894_harry_hone ---|1914| 1894_ada_phillips
    1914_harry_hone["Harry Hone<br/>b. 1914 Q3"]:::person
    1894_ada_phillips --> 1914_harry_hone

    %% GEORGE HONE AND YOLANDA CHALIER
    %% Yolanda: child George born 1933 => parent estimated 1873–1918.
    1873_1918_yolanda_chalier["Yolanda (Chalier)<br/>b. c. 1873–1918"]:::person
    1899_george_hone ---|married| 1873_1918_yolanda_chalier
    %% Undated children: father 1899 => 1914–1959;
    %% mother estimated 1873–1918 => 1888–1978;
    %% intersection 1914–1959. No sibling-order assumption.
    1914_1959_violet_hone["Violet Hone<br/>b. c. 1914–1959"]:::person
    1933_george_hone["George Hone<br/>b. 1933"]:::person
    1914_1959_doris_hone["Doris Hone<br/>b. c. 1914–1959"]:::person
    1914_1959_arthur_hone["Arthur Hone<br/>b. c. 1914–1959"]:::person
    1873_1918_yolanda_chalier --> 1914_1959_violet_hone & 1933_george_hone & 1914_1959_doris_hone & 1914_1959_arthur_hone
    %% Source records an unnamed spouse and daughter Jacqueline.
    %% Only the named parent is drawn; father 1933 => child 1948–1993.
    1948_1993_jacqueline_hone["Jacqueline Hone<br/>b. c. 1948–1993"]:::person
    1933_george_hone --> 1948_1993_jacqueline_hone

    %% ELLIS AND ASHBY FAMILIES
    %% James Ellis: daughter Lilian born 1899 => parent 1839–1884.
    1839_1884_james_ellis["James Ellis<br/>b. c. 1839–1884"]:::person
    1870_1871_edith_hone ---|married| 1839_1884_james_ellis
    1899_lilian_ellis["Lilian Edith Bethia (Ellis)<br/>b. 1899 Apr 09"]:::person
    1839_1884_james_ellis --> 1899_lilian_ellis
    1892_james_ashby["James Henry William Ashby<br/>b. 1892"]:::person
    1899_lilian_ellis ---|married| 1892_james_ashby
    1921_arthur_ashby["Arthur Ashby<br/>b. 1921"]:::person
    1923_cyril_ashby["Cyril Ashby<br/>b. 1923"]:::person
    1924_david_ashby["David Ashby<br/>b. 1924"]:::person
    1926_edwin_ashby["Edwin Ashby<br/>b. 1926"]:::person
    1928_donald_ashby["Donald Ashby<br/>b. 1928; d. 1932"]:::person
    1930_raymond_ashby["Raymond Ashby<br/>b. 1930"]:::person
    1892_james_ashby --> 1921_arthur_ashby & 1923_cyril_ashby & 1924_david_ashby & 1926_edwin_ashby & 1928_donald_ashby & 1930_raymond_ashby

    %% BEADELL FAMILY
    %% Nathaniel: age 16 in 1881 => 1864–1865.
    %% Samuel's child-based estimate depends on that range: 1804–1850.
    %% Marriage 1860 => 1820–1844; intersection 1820–1844.
    1820_1844_samuel_beadell["Samuel Beadell<br/>b. c. 1820–1844"]:::person
    %% Married 1860 Q2, Marylebone.
    1842_frances_hone ---|1860| 1820_1844_samuel_beadell
    1864_1865_nathaniel_beadell["Nathaniel Beadell<br/>b. c. 1864–1865"]:::person
    1820_1844_samuel_beadell --> 1864_1865_nathaniel_beadell

    %% NATHANIEL JOHNSON HONE'S DESCENDANTS
    %% Only named parents drawn; the source leaves their spouses unnamed.
    %% Nathaniel 1844 => Frank estimated 1859–1904.
    1859_1904_frank_hone["Frank Sandland Hone<br/>b. c. 1859–1904"]:::person
    1844_nathaniel_hone --> 1859_1904_frank_hone
    %% Brian depends on Frank's estimated birth: [1859+15,1904+60].
    1874_1964_brian_hone["Brian William Hone<br/>b. c. 1874–1964"]:::person
    1859_1904_frank_hone --> 1874_1964_brian_hone

    %% EMMA HONE AND CARL HUGO HAHN
    1774_carl_hahn["Carl Peter Hahn<br/>b. 1774; d. 1863"]:::person
    1818_carl_hahn["Carl Hugo Hahn<br/>b. 1818 Oct 18; d. 1895"]:::person
    1774_carl_hahn --> 1818_carl_hahn
    %% Married 1843 Oct 03, Windhoek.
    1814_emma_hone ---|1843| 1818_carl_hahn
    1844_josaphat_hahn["Josaphat Hahn<br/>b. 1844 Aug 07"]:::person
    1846_carl_hahn["Carl Hugo Hahn<br/>b. 1846"]:::person
    1848_elieser_hahn["Elieser Traugott Hahn<br/>b. 1848 Aug 15; d. 1939"]:::person
    1850_emma_hahn["Emma Marguerite (Hahn)<br/>b. 1850 Jul 06; d. 1906"]:::person
    1818_carl_hahn --> 1844_josaphat_hahn & 1846_carl_hahn & 1848_elieser_hahn & 1850_emma_hahn

    %% CARL HUGO HAHN AND ANNIE VON LINSINGEN
    %% Ernst: death 1918 age 28 => 1889–1890.
    %% Benno: death 1917 age 17 => 1899–1900.
    %% Annie: those age-derived child ranges plus Alfred born 1902
    %% give parental intersection 1842–1875.
    %% Marriage 1881 => 1841–1865; final intersection 1842–1865.
    %% Source variation Anna/Annie is retained here as Annie.
    1842_1865_annie_vonlinsingen["Annie Judith Julie Auguste (von Linsingen)<br/>b. c. 1842–1865"]:::person
    %% Married 1881 Jan 25.
    1846_carl_hahn ---|1881| 1842_1865_annie_vonlinsingen
    1902_alfred_hahn["Alfred Friedrich Linsingen Hahn<br/>b. 1902 Jan 01"]:::person
    1896_carl_hahn["Carl Hugo Linsingen 'Cocky' Hahn<br/>b. 1896 Sep 26?"]:::person
    1889_1890_ernst_hahn["Ernst Albert Linsingen Hahn<br/>b. c. 1889–1890; d. 1918"]:::person
    1899_1900_benno_hahn["Benno Oscar Linsingen Hahn<br/>b. c. 1899–1900; d. 1917"]:::person
    1842_1865_annie_vonlinsingen --> 1902_alfred_hahn & 1896_carl_hahn & 1889_1890_ernst_hahn & 1899_1900_benno_hahn

    %% ELIESER TRAUGOTT HAHN AND ROSALIE PALING
    1850_rosalie_paling["Rosalie Sophie (Paling)<br/>b. 1850 Oct 23; d. 1905"]:::person
    1848_elieser_hahn ---|married| 1850_rosalie_paling
    1874_gotthilft_hahn["Gotthilft Traugott Hahn<br/>b. 1874 Feb 13; d. 1874"]:::person
    %% Dual-calendar day alternatives preserved.
    1875_gotthilft_hahn["Gotthilft Traugott Hahn<br/>b. 1875 Feb 01 / 1875 Feb 13"]:::person
    1876_wilhelm_hahn["Wilhelm Hugo Hahn<br/>b. 1876 Aug 30; d. 1894"]:::person
    1878_emma_hahn["Emma Julie (Hahn)<br/>b. 1878 Aug 03; d. 1955"]:::person
    1879_august_hahn["August Daniel Theodor Johannes Hahn<br/>b. 1879 Aug 25; d. 1924"]:::person
    1881_georg_hahn["Georg Bruno Martin Hahn<br/>b. 1881 Aug 24; d. 1959"]:::person
    1883_magdalene_hahn["Magdalene Elisabeth Seni (Hahn)<br/>b. 1883 Aug 22; d. 1943"]:::person
    1886_carl_hahn["Carl Hugo Hahn<br/>b. 1886 Sep 22 / 1886 Oct 04; d. 1957"]:::person
    1888_natalie_hahn["Natalie Friederike Sophie Hahn<br/>b. 1888 Feb 08; d. 1952"]:::person
    1889_maria_hahn["Maria Hahn<br/>b. 1889 Apr 30"]:::person
    1892_maria_hahn["Maria Elisabeth Margarete (Hahn)<br/>b. 1892 Jun 24; d. 1953"]:::person
    1850_rosalie_paling --> 1874_gotthilft_hahn & 1875_gotthilft_hahn & 1876_wilhelm_hahn & 1878_emma_hahn & 1879_august_hahn & 1881_georg_hahn & 1883_magdalene_hahn & 1886_carl_hahn & 1888_natalie_hahn & 1889_maria_hahn & 1892_maria_hahn
    1878_gerta_vonzurmhlen["Gerta Ernestine Anna (von zur M'hlen)<br/>b. 1878 Aug 28; d. 1974"]:::person
    %% Married 1903 Aug 29 / 1903 Sep 12, Tallinn.
    1875_gotthilft_hahn ---|1903| 1878_gerta_vonzurmhlen
    1878_alma_vonbrggen["Alma Gabriele Charlotte (von Br'ggen)<br/>b. 1878 Jul 30; d. 1951"]:::person
    1879_august_hahn ---|married| 1878_alma_vonbrggen
    1886_elisabeth_silverberg["Elisabeth Lina (Silverberg)<br/>b. 1886 Mar 22"]:::person
    %% Married 1911 Jun 19.
    1881_georg_hahn ---|1911| 1886_elisabeth_silverberg
    1886_alexandrine_vonbaggehufvudt["Alexandrine Pauline Erika (von Baggehufvudt)<br/>b. 1886 Nov 22; d. 1942"]:::person
    %% Married 1910 Dec 09 / 1910 Dec 22, Tallinn.
    1886_carl_hahn ---|1910| 1886_alexandrine_vonbaggehufvudt
    1887_franz_hannula["Franz Edward Hannula<br/>b. 1887 Aug 14"]:::person
    %% Married 1914 Aug 23, Pargas.
    1892_maria_hahn ---|1914| 1887_franz_hannula

    %% SIELMANN FAMILY
    1875_woldemar_sielmann["Woldemar Paul Sielmann<br/>b. 1875 Mar 23; d. 1942"]:::person
    %% Married 1902 Aug 19, Tallinn.
    1878_emma_hahn ---|1902| 1875_woldemar_sielmann
    1904_burchard_sielmann["Burchard Traugott Sielmann<br/>b. 1904 Jul 21 / 1904 Aug 03; d. 1954"]:::person
    1907_heinrich_sielmann["Heinrich Wolfgang Traugott Sielmann<br/>b. 1907 Feb 06; d. 1945"]:::person
    1910_hildegard_sielmann["Hildegard (Sielmann)<br/>b. 1910 Jun 01; d. 1964"]:::person
    1913_marie_sielmann["Marie (Sielmann)<br/>b. 1913 Dec 13"]:::person
    1875_woldemar_sielmann --> 1904_burchard_sielmann & 1907_heinrich_sielmann & 1910_hildegard_sielmann & 1913_marie_sielmann
    1908_marianne_vongrgens["Marianne (von G'rgens)<br/>b. 1908 Apr 20; d. 1965"]:::person
    %% Married 1934 Mar 25, Frankfurt am Main.
    1904_burchard_sielmann ---|1934| 1908_marianne_vongrgens
    1910_martha_dietrich["Martha (Dietrich)<br/>b. 1910 Apr 15"]:::person
    %% Married 1936 Sep 06.
    1907_heinrich_sielmann ---|1936| 1910_martha_dietrich
    1912_werner_hesseken["Werner Hesseken<br/>b. 1912 Feb 02; d. 1964"]:::person
    1910_hildegard_sielmann ---|married| 1912_werner_hesseken
    1910_harald_donath["Harald Donath<br/>b. 1910 Dec 20; d. 1944"]:::person
    %% Married 1938 Oct 30, Frankfurt am Main.
    1913_marie_sielmann ---|1938| 1910_harald_donath

    %% BEIDERBECKE FAMILY
    1845_heinrich_beiderbecke["Heinrich Beiderbecke<br/>b. 1845; d. 1936"]:::person
    %% Married 1875 Jul 06; text is displaced alongside Charlotte in source.
    1850_emma_hahn ---|1875| 1845_heinrich_beiderbecke
    1876_frederick_beiderbecke["Frederick Christian Beiderbecke<br/>b. 1876"]:::person
    1845_heinrich_beiderbecke --> 1876_frederick_beiderbecke
    %% Catherine: child Joseph born 1911 => parent estimated 1851–1896.
    1851_1896_catherine_thum["Catherine (Thum)<br/>b. c. 1851–1896"]:::person
    1876_frederick_beiderbecke ---|married| 1851_1896_catherine_thum
    %% Source spells this descendant's surname Beidebecker.
    1911_joseph_beidebecker["Joseph Thum Beidebecker<br/>b. 1911; d. 1995"]:::person
    1851_1896_catherine_thum --> 1911_joseph_beidebecker

    %% ELLEN HONE AND JOSEPH SIMMONDS SOUL
    %% Conditional spouse estimate from Ellen born 1822:
    %% both marrying aged 16–40 => 1798–1846; not source birth evidence.
    1798_1846_joseph_soul["Joseph Simmonds Soul<br/>b. c. 1798–1846"]:::person
    1822_ellen_hone ---|married| 1798_1846_joseph_soul

    %% ALICE HONE'S FIRST MARRIAGE
    %% Agnes: age 20 in 1871 => 1850–1851.
    %% Jean-Baptiste: Alice born 1847 => 1787–1832;
    %% Agnes age-derived 1850–1851 => 1790–1836;
    %% parent-based intersection 1790–1832.
    1790_1832_jean_baptiste_lovati["Jean-Baptiste Lovati<br/>b. c. 1790–1832"]:::person
    %% First marriage; year unknown.
    1825_alice_hone ---|married| 1790_1832_jean_baptiste_lovati
    1847_alice_lovati["Alice Romola Lovati<br/>b. 1847 Q4; d. 1851"]:::person
    1850_1851_agnes_lovati["Agnes Lovati<br/>b. c. 1850–1851"]:::person
    1790_1832_jean_baptiste_lovati --> 1847_alice_lovati & 1850_1851_agnes_lovati
    %% Agnes later Salme; no spouse is named.

    %% ALICE HONE'S SECOND MARRIAGE
    %% Emma: age 12 in 1871 => 1858–1859.
    %% Henri-Auguste: Emma age-derived 1858–1859 => 1798–1844;
    %% Angeline born 1869 => 1809–1854; intersection 1809–1844.
    1809_1844_henri_auguste_fourdinois["Henri-Auguste Fourdinois<br/>b. c. 1809–1844"]:::person
    %% Second marriage; year unknown.
    1825_alice_hone ---|married| 1809_1844_henri_auguste_fourdinois
    1858_1859_emma_fourdinois["Emma Fourdinois<br/>b. c. 1858–1859"]:::person
    1869_angeline_fourdinois["Angeline Fourdinois<br/>b. 1869 Jun 29"]:::person
    1809_1844_henri_auguste_fourdinois --> 1858_1859_emma_fourdinois & 1869_angeline_fourdinois
    %% Emma later Roulez; Angeline later Sanze. No spouses named.

    %% JOSEPH HONE'S FIRST MARRIAGE
    %% Ann: death 1839, age 61 => 1777–1778.
    1777_1778_ann_lamport["Ann (Lamport)<br/>b. c. 1777–1778; d. 1839"]:::person
    %% First marriage: 1802 Sep 11, St Anne's Soho.
    1783_joseph_hone ---|1802| 1777_1778_ann_lamport
    %% Hannah and Mary Ann: father 1783 => 1798–1843;
    %% mother age-derived 1777–1778 => 1792–1838;
    %% parent-based intersection 1798–1838.
    %% Hannah marriage 1826 => 1786–1810; final 1798–1810.
    %% Mary Ann marriage 1825 => 1785–1809; final 1798–1809.
    1798_1810_hannah_hone["Hannah (Hone)<br/>b. c. 1798–1810"]:::person
    1798_1809_mary_hone["Mary Ann (Hone)<br/>b. c. 1798–1809; d. 1850"]:::person
    %% Martha Ann: death 1839, age 28 => 1810–1811.
    1810_1811_martha_hone["Martha Ann Hone<br/>b. c. 1810–1811; d. 1839"]:::person
    1777_1778_ann_lamport --> 1798_1810_hannah_hone & 1798_1809_mary_hone & 1810_1811_martha_hone
    %% William: marriage 1826 => estimated 1786–1810.
    1786_1810_william_fletcher["William Fletcher<br/>b. c. 1786–1810"]:::person
    %% Married 1826 Dec 26, Hobart Town.
    1798_1810_hannah_hone ---|1826| 1786_1810_william_fletcher
    %% James: marriage 1825 => estimated 1785–1809.
    1785_1809_james_hobbs["James Hobbs<br/>b. c. 1785–1809"]:::person
    %% Married 1825 Jul 27.
    1798_1809_mary_hone ---|1825| 1785_1809_james_hobbs

    %% JOSEPH HONE'S SECOND MARRIAGE
    %% Elizabeth: children 1842 and 1848 => parent 1788–1827;
    %% marriage 1840 => 1800–1824; intersection 1800–1824.
    1800_1824_elizabeth_rowe["Elizabeth Augusta (Rowe)<br/>b. c. 1800–1824"]:::person
    %% Her father W H Rowe depends on her estimated birth:
    %% [1800-60,1824-15] => 1740–1809.
    1740_1809_wh_rowe["W H Rowe<br/>b. c. 1740–1809"]:::person
    1740_1809_wh_rowe --> 1800_1824_elizabeth_rowe
    %% Second marriage: 1840 May 21, Hobart Town.
    %% Joseph was already widowed; do not apply first-marriage ages to him.
    1783_joseph_hone ---|1840| 1800_1824_elizabeth_rowe
    1842_joseph_hone["Joseph Hone<br/>b. 1842 May 01; d. 1842"]:::person
    1848_joseph_hone["Joseph William James Hone<br/>b. 1848 Jun 04"]:::person
    1800_1824_elizabeth_rowe --> 1842_joseph_hone & 1848_joseph_hone
    %% Joseph born 1783 was approximately 64–65 at the 1848 birth.
    %% This exceeds the provisional parental ceiling; retain documented dates.

    linkStyle default stroke:#555
```
