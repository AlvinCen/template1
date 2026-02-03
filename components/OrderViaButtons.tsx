import { SiWhatsapp, SiShopee, SiTiktok } from 'react-icons/si';
import { RiShoppingBag3Fill } from 'react-icons/ri';
import { links } from '../data/links';
import { SHOP_INFO } from '../constants';

const OrderViaButtons = () => {
    const orderChannels = [
        {
            name: 'WhatsApp',
            icon: SiWhatsapp,
            url: links.order.whatsapp ? `https://wa.me/${links.order.whatsapp}?text=${encodeURIComponent(SHOP_INFO.whatsappMessage)}` : null,
            bgColor: 'bg-green-600 hover:bg-green-700',
            disabledBg: 'bg-gray-300'
        },
        {
            name: 'Shopee',
            icon: SiShopee,
            url: links.order.shopee,
            bgColor: 'bg-orange-600 hover:bg-orange-700',
            disabledBg: 'bg-gray-300'
        },
        {
            name: 'Tokopedia',
            icon: RiShoppingBag3Fill,
            url: links.order.tokopedia,
            bgColor: 'bg-green-500 hover:bg-green-600',
            disabledBg: 'bg-gray-300'
        },
        {
            name: 'TikTok',
            icon: SiTiktok,
            url: links.order.tiktok,
            bgColor: 'bg-black hover:bg-gray-800',
            disabledBg: 'bg-gray-300'
        },
    ];

    return (
        <div className="mt-6">
            <p className="text-gray-300 text-sm mb-3 font-medium">Order via:</p>
            <div className="flex flex-wrap gap-3">
                {orderChannels.map((channel) => {
                    const Icon = channel.icon;
                    const isDisabled = !channel.url;

                    if (isDisabled) {
                        return (
                            <div
                                key={channel.name}
                                className="relative group"
                            >
                                <button
                                    disabled
                                    className={`${channel.disabledBg} text-gray-500 font-semibold py-2 px-4 rounded-lg flex items-center gap-2 cursor-not-allowed opacity-60`}
                                >
                                    <Icon size={18} />
                                    {channel.name}
                                </button>
                                <div className="absolute hidden group-hover:block bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap -bottom-8 left-1/2 transform -translate-x-1/2 z-10">
                                    Link menyusul
                                </div>
                            </div>
                        );
                    }

                    return (
                        <a
                            key={channel.name}
                            href={channel.url!}
                            target="_blank"
                            rel="noopener noreferrer"
                            className={`${channel.bgColor} text-white font-semibold py-2 px-4 rounded-lg flex items-center gap-2 transition-colors shadow-md`}
                        >
                            <Icon size={18} />
                            {channel.name}
                        </a>
                    );
                })}
            </div>
        </div>
    );
};

export default OrderViaButtons;
