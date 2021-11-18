-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2021 at 10:29 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admuname` varchar(40) NOT NULL,
  `admupass` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admuname`, `admupass`) VALUES
('mukolop', 'mukolop');

-- --------------------------------------------------------

--
-- Table structure for table `admissionnumber`
--

CREATE TABLE `admissionnumber` (
  `admno` int(11) NOT NULL,
  `dated` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admissionnumber`
--

INSERT INTO `admissionnumber` (`admno`, `dated`) VALUES
(1213, '2010-01-21'),
(1901, '2010-01-21'),
(1902, '2010-01-21'),
(1905, '2010-01-21'),
(1908, '2010-01-21'),
(1909, '2010-01-21'),
(2345, '2010-01-21'),
(2347, '2010-01-21'),
(3030, '2019-07-09'),
(3412, '2010-01-21'),
(3420, '2010-01-21'),
(3430, '2021-11-01'),
(3456, '2010-01-21'),
(3636, '2019-05-10'),
(4000, '2010-01-21'),
(4040, '2010-01-21'),
(4041, '2021-11-18'),
(4042, '2021-11-18'),
(4540, '2021-11-17'),
(4545, '2019-04-19'),
(6767, '2019-05-20'),
(7777, '2019-04-19'),
(7878, '2019-05-20'),
(7902, '2021-10-14');

-- --------------------------------------------------------

--
-- Table structure for table `bookinfo`
--

CREATE TABLE `bookinfo` (
  `isbnno` int(11) NOT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `edno` int(11) DEFAULT NULL,
  `shelfno` int(11) DEFAULT NULL,
  `dated` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookinfo`
--

INSERT INTO `bookinfo` (`isbnno`, `subject`, `author`, `edno`, `shelfno`, `dated`) VALUES
(5051, 'python ', 'calvin mark', 7, 2, '2019-04-24'),
(5067, 'SQL', 'Jasmin', 6, 6, '2008-05-19'),
(6060, 'Maths', 'Janes', 2, 4, '2019-04-24'),
(6061, 'Java', 'Ashley', 2, 4, '2019-04-24'),
(6062, 'AI', 'Mark', 2, 4, '2019-04-24'),
(6063, 'Data science', 'Wack', 2, 4, '2019-04-24'),
(7071, 'Linus', 'Christine', 4, 4, '2019-04-24'),
(7072, 'We design', 'John', 4, 4, '2019-04-24'),
(8082, 'electrons', 'steph', 4, 12, '2021-11-18');

-- --------------------------------------------------------

--
-- Table structure for table `borrowbook`
--

CREATE TABLE `borrowbook` (
  `isbnno` int(11) NOT NULL,
  `admno` int(11) DEFAULT NULL,
  `dated` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `borrowbook`
--

INSERT INTO `borrowbook` (`isbnno`, `admno`, `dated`) VALUES
(5051, 2020, '2021-10-14'),
(6063, 2020, '2019-04-25'),
(8082, 7777, '2021-11-18');

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE `librarian` (
  `staffno` int(11) NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `sname` varchar(20) DEFAULT NULL,
  `phoneno` int(11) DEFAULT NULL,
  `upass` varchar(20) DEFAULT NULL,
  `cupass` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `librarian`
--

INSERT INTO `librarian` (`staffno`, `fname`, `sname`, `phoneno`, `upass`, `cupass`) VALUES
(2121, 'beth', 'mbone', 76540023, 'beth', 'beth'),
(3040, 'mcjames', 'simon', 789543212, 'james', 'james'),
(3131, 'johnse', 'johnse', 9876543, 'james', 'james'),
(3232, 'johnson', 'wavu', 754321897, 'mwasi', 'mwasi'),
(3333, 'johnse', 'johnse', 9876543, 'james', 'james'),
(8081, 'faith', 'eve', 78654567, 'eve23', 'eve23');

-- --------------------------------------------------------

--
-- Table structure for table `receive`
--

CREATE TABLE `receive` (
  `isbnno` int(11) DEFAULT NULL,
  `admno` int(11) DEFAULT NULL,
  `dated` date DEFAULT NULL,
  `dated1` date DEFAULT NULL,
  `fine` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receive`
--

INSERT INTO `receive` (`isbnno`, `admno`, `dated`, `dated1`, `fine`) VALUES
(5067, 2020, '2021-11-17', '2021-11-17', 0),
(5067, 7777, '2021-11-17', '2021-11-17', 0),
(8082, 1901, '2021-11-18', '2021-11-18', 0);

-- --------------------------------------------------------

--
-- Table structure for table `reservebook`
--

CREATE TABLE `reservebook` (
  `isbnno` int(11) NOT NULL,
  `admno` int(11) DEFAULT NULL,
  `dated` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reservebook`
--

INSERT INTO `reservebook` (`isbnno`, `admno`, `dated`) VALUES
(6060, 7777, '2021-10-14'),
(7071, 7777, '2021-10-14');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `admno` int(11) NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `sname` varchar(20) DEFAULT NULL,
  `gender` varchar(11) DEFAULT NULL,
  `phoneno` int(11) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `upass` varchar(20) DEFAULT NULL,
  `cupass` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`admno`, `fname`, `sname`, `gender`, `phoneno`, `course`, `upass`, `cupass`) VALUES
(1213, 'macy', 'michael', 'MALE', 34129654, 'CS', 'macy', 'macy'),
(1901, 'jentrix', 'macy', 'FEMALE', 766548890, 'Telecom', 'macy', 'macy'),
(2020, 'mcjemo', 'ngumi', 'Male', 9865432, 'IT', 'jemo', 'jemo'),
(3636, 'mctabby', 'stabby', 'Female', 9876543, 'market', 'mcpeter', 'mcpeter'),
(7777, 'peter', 'jones', 'Male', 9876543, 'maths', 'james', 'james');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admuname`);

--
-- Indexes for table `admissionnumber`
--
ALTER TABLE `admissionnumber`
  ADD PRIMARY KEY (`admno`);

--
-- Indexes for table `bookinfo`
--
ALTER TABLE `bookinfo`
  ADD PRIMARY KEY (`isbnno`);

--
-- Indexes for table `borrowbook`
--
ALTER TABLE `borrowbook`
  ADD PRIMARY KEY (`isbnno`);

--
-- Indexes for table `librarian`
--
ALTER TABLE `librarian`
  ADD PRIMARY KEY (`staffno`);

--
-- Indexes for table `reservebook`
--
ALTER TABLE `reservebook`
  ADD PRIMARY KEY (`isbnno`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`admno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
