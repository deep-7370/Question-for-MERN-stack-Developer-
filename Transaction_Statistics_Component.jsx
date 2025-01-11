function TransactionStatistics({ selectedMonth }) {
    const [stats, setStats] = useState({
      totalSale: 0,
      soldItems: 0,
      unsoldItems: 0
    });
  
    useEffect(() => {
      fetchMonthlyStats(selectedMonth);
    }, [selectedMonth]);
  
    const fetchMonthlyStats = async (month) => {
      const response = await api.getMonthlyStatistics(month);
      setStats(response.data);
    };
  
    return (
      <StatisticsCard 
        totalSale={stats.totalSale}
        soldItems={stats.soldItems}
        unsoldItems={stats.unsoldItems}
      />
    );
  }